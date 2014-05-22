
Fedora Cloud Features
=====================

A simple example of how

  - gherkin can be used to describe required features
  - python-behave does the parsing
  - python-virtexpect provides interaction with the VMs

All in all a way to realize autoamtic testing of cloud (and similar) images.


How to run
----------

Download the Fedora cloud image to ~/Downloads, then

    $ pkcon install -y python-behave qemu-kvm
    $ behave .


References
----------

Some helpful links

  - http://pythonhosted.org/behave/gherkin.html
  - http://fedoraproject.org/en/get-fedora#clouds
  - https://github.com/fabiand/imgbased/blob/master/tests/functional/virtexpect.py

