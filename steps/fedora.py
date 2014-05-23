
from behave import *
import virtexpect as vms
import os.path

VMFILE = "./Fedora-x86_64-20-20140407-sda.qcow2"

@given(u'a default VM')
def step_impl(ctx):
    ctx.instance = vms.FedoraInstance(VMFILE)

@given(u'the latest Fedora cloud image')
def step_impl(context):
    assert os.path.exists(VMFILE), "Please download the latest Fedora cloud image to " + VMFILE

@given(u'that the VM is turned on')
def step_impl(ctx):
    ctx.instance.spawn()

@step(u'we wait for {timeout} seconds at most')
def step_impl(ctx, timeout):
    ctx.last_timeout = float(timeout)

@then(u'we expect the bootloader prompt to appear')
def step_impl(ctx):
    pass
    # depends on https://fedorahosted.org/cloud/ticket/60
    #ctx.instance.expect(".*Welcome to Fedora.*", timeout=ctx.last_timeout)

@given(u'that the bootloader passed')
def step_impl(ctx):
    pass
    # depends on https://fedorahosted.org/cloud/ticket/60
    #ctx.instance.expect("Loading /boot/vmlinuz", timeout=ctx.last_timeout)

@then(u'we expect the kernel to be loaded')
def step_impl(ctx):
    ctx.instance.expect(".*Linux version.*", timeout=ctx.last_timeout)

@then(u'systemd to be running')
def step_impl(ctx):
    ctx.instance.expect("systemd [0-9]+ running in system mode", timeout=ctx.last_timeout)

@then(u'we expect a login prompt')
def step_impl(ctx):
    ctx.instance.expect("(?i)login:", timeout=ctx.last_timeout)

