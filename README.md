# UbuntuCockpit (UBU)

## Features
UbuntuCockpit is a Ubuntu chroot subsystem for Enigma2 based settop boxes. It provides access to the vast Ubuntu ecosystem.

## Use Case
One popular use case is: Development environment including git on the open settopbox.


## Prerequisite
- A mounted disk at /media/hdd (the default installation directory). To use another directory, define it in /etc/enigma2/ubuntucockpit.cfg before installing, a one-liner like: /media/usb
- A folder git in the installation directory: it is shared with the Ubuntu subsystem as /root/git

See the wiki for details: https://github.com/xcentaurix/UbuntuCockpit/wiki

## Usage
- To enter the ubuntu subsystem open a telnet session and enter the command: ubuntu
- To leave the ubuntu subsystem enter the command: exit

## Installation
The Ubuntu subsystem is installed persistantly. So, it will survive the removal of the Enigma2 plugin, and will not be re-installed during plugin installation if the Ubuntu subsystem directory exists. So, the user has to remove the Ubuntu subsystem directory manually, if they want to re-install the subsystem.

The scripts of the plugin (root/*_chroot) and the library git needs (getrandom_stub.so) are copied into the Ubuntu subsystem at every plugin installation, also if the subsystem exists already. So, an update of the plugin brings their new versions along.

## Limitations
- Tested on OpenViX and OpenATV with DM900.

## Installation
The plugin will be installed as a dependency, no explicit installation required.

## Wiki
- https://github.com/xcentaurix/UbuntuCockpit/wiki
