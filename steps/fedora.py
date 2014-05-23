from behave import step, given, then
import virtexpect as vms
from os import system

DEFAULT_TIMEOUT = 60


@given(u'a VM is downloaded from "{url}"')
def vm_is_downloaded_from(ctx, url):
    try:
        file_path = url.split('/')[-1]
        system("curl -L -O %s" % url)
        ctx.instance = vms.FedoraInstance(file_path)
    except Exception as e:
        raise Exception("Image %s cannot be downloaded: %s" % (url, str(e)))


@step(u'the VM is turned on')
def vm_is_turned_on(ctx):
    ctx.instance.spawn()


@then(u'we expect the bootloader prompt to appear')
@then(u'we expect the bootloader prompt to appear in {timeout} seconds at most')
def bootloader_appear(ctx, timeout=DEFAULT_TIMEOUT):
    pass
    # depends on https://fedorahosted.org/cloud/ticket/60
    #ctx.instance.expect(".*Welcome to Fedora.*", timeout=float(timeout))


@then(u'we expect the kernel to be loaded')
@then(u'we expect the kernel to be loaded in {timeout} seconds at most')
def kernel_loaded(ctx, timeout=DEFAULT_TIMEOUT):
    ctx.instance.expect(".*Linux version.*", timeout=float(timeout))


@then(u'systemd to be running')
@then(u'systemd to be running in {timeout} seconds at most')
def systemd_is_running(ctx, timeout=DEFAULT_TIMEOUT):
    ctx.instance.expect("systemd [0-9]+ running in system mode", float(timeout))


@then(u'we expect a login prompt to appear')
@then(u'we expect a login prompt to appear in {timeout} seconds at most')
def login_prompt_appeared(ctx, timeout=DEFAULT_TIMEOUT):
    ctx.instance.expect("(?i)login:", timeout=float(timeout))
