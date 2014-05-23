
Fedora Cloud Features
=====================

A simple example of how

  - gherkin can be used to describe required features
  - python-behave does the parsing
  - python-virtexpect provides interaction with the VMs

All in all a way to realize automatic testing of cloud (and similar) images.

Pros:

  - Mainly reusing existing technologies
  - Simple
  - Separation of concerns

Cons:

  - Currently local only (extend to use libvirt, OS, or RHEV as a backend?)


How to run
----------

    $ pkcon install -y python-behave qemu-kvm
    $ curl -O http://download.fedoraproject.org/pub/fedora/linux/updates/20/Images/x86_64/Fedora-x86_64-20-20140407-sda.qcow2
    $ behave .


References
----------

Some helpful links

  - http://pythonhosted.org/behave/gherkin.html
  - http://fedoraproject.org/en/get-fedora#clouds
  - https://github.com/fabiand/imgbased/blob/master/tests/functional/virtexpect.py

