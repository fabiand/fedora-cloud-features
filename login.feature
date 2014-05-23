
Feature: Basic bootability
  Cover the basic boot process. Ensure that we see a bootloader
  and a login prompt is displayed.

  Background: Some virtual machine with Fedora
        Given a default VM
          and the latest Fedora cloud image
          and that the VM is turned on

  Scenario: A bootloader is expected right after boot
       When we wait for 5 seconds at most
       Then we expect the bootloader prompt to appear

  Scenario: The kernel and systemd is started
       When we wait for 30 seconds at most
       Then we expect the kernel to be loaded
        and systemd to be running

  Scenario: A login prompt is displayed
       When we wait for 70 seconds at most
       Then we expect a login prompt
