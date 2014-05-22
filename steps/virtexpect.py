#!/usr/bin/env python
"""
A simple class to do some kind of functional tests on VM images.
It works by redireting the console of a VM to stdio, which is then
handled with pexpect.
"""
import pexpect
import sys
import logging


class Instance(object):
    log = None
    image = None

    child = None

    mount_tag = "hostos"
    shared_path = None
    guestpath_to_host = "/tmp/%s" % mount_tag

    def __init__(self, image, shared_path=None):
        assert image
        self.image = image
        self.shared_path = shared_path
        self.log = logging.getLogger(__name__)

    def spawn(self):
        cmd = self.qemu_cmd(self.image)
        self.log.debug("Launching: %s" % cmd)
        self.child = pexpect.spawn(cmd)
        self.child.logfile = sys.stdout
        self.child.setecho(False)
	assert self.child

    def qemu_cmd(self, image):
        cmd = "qemu-kvm"
        cmd += " -m 1024 -smp 4 -serial stdio -net user -net nic"
        cmd += " -snapshot -hda %s" % image
        cmd += " -watchdog-action poweroff"

        if self.shared_path:
            self.log.debug("Using shared path: %s" % self.shared_path)
            cmd += " -virtfs local,id=virtpexpect,"
            cmd += "path=%s," % self.shared_path
            cmd += "mount_tag=%s," % self.mount_tag
            cmd += "security_model=none"

        return cmd

    def expect(self, *args, **kwargs):
        return self.child.expect(*args, **kwargs)

    def sendline(self, *args, **kwargs):
        return self.child.sendline(*args, **kwargs)

    def _wait_command(self, cmd):
        self.child.sendline(cmd)
        self.child.expect("[$#] ")  # ("^\[.*\]#")

    def mount_hostos(self):
        self._wait_command("mkdir %s" % self.guestpath_to_host)
        self._wait_command("mount -t 9p -o trans=virtio %s %s" %
                           (self.mount_tag, self.guestpath_to_host))
        self._wait_command("findmnt %s" % self.guestpath_to_host)

    def enter_shared_path(self):
        self._wait_command("cd %s" % self.guestpath_to_host)


class FedoraInstance(Instance):
    """Makes more assumptions
    """
    def __enter__(self):
        self.spawn()
        return self

    def __exit__(self, *args, **kwargs):
        self.poweroff()

    def poweroff(self):
        if self.child.isalive():
            self.child.sendline('init 0')
            self.child.close()

        if self.child.isalive():
            self.log.warn('Child did not exit gracefully.')
        else:
            self.log.debug('Child exited gracefully.')

    def login(self, username, password):
        self.expect('(?i)login:')
        self.sendline(username)
        self.expect('(?i)password:')
        self.sendline(password)
        self.expect('[#$] ')

    def logout(self):
        self.child.sendline('exit')
        self.child.expect('(?i)login:')
