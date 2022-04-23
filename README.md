# XANDER
A modular network device configuration builder.
## Installation
```
  $ cd XANDER
  $ python3 setup.py install
```
## Command Line Operations
### Build A Config
```
  $ xander config build -d <DeviceName> 

  Optional args:
    -v / --vendor - defaults to juniper if not specified
        only juniper currently supported
    -s / --section - defaults to all if not specified
        available sections:
            * all
            * acls
            * interfaces
            * macsec
            * policies
            * routing
            * system
```