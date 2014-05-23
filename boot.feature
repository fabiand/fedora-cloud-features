
Feature: Basic bootability
  Cover the basic boot process. Ensure that we see a bootloader
  and a login prompt is displayed.

  Background: Some virtual machine with Fedora

  Scenario Outline: Login prompt
      Given a VM is downloaded from "<URL>"

       When the VM is turned on
       Then we expect the bootloader prompt to appear in 30 seconds at most
        And we expect the kernel to be loaded in 60 seconds at most
        And systemd to be running
        And we expect a login prompt to appear in 480 seconds at most

      Examples:
        | URL                                                                                                             |
        | http://download.fedoraproject.org/pub/fedora/linux/updates/20/Images/x86_64/Fedora-x86_64-20-20140407-sda.qcow2 |
        | http://download.fedoraproject.org/pub/fedora/linux/updates/20/Images/i386/Fedora-i386-20-20140407-sda.qcow2     |
