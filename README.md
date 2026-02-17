# UbuntuCockpit (UBU)

## Features
UbuntuCockpit is a Ubuntu chroot subsystem for Enigma2 based settop boxes. It provides access to the vast Ubuntu ecosystem.

## Use Case
One popular use case is: Development environment including git on the open settopbox.


## Prerequisite
- Define installation directory in /etc/enigma2/ubuntucockpit.cfg, a one-liner like: /media/usb

## Usage
- To enter the ubuntu subsystem open a telnet session and enter the command: ubuntu
- To leave the ubuntu subsystem enter the command: exit

## Installation
The Ubuntu subsystem is installed persistantly. So, it will survive the removal of the Enigma2 plugin, and will not be re-installed during plugin installation if the Ubuntu subsystem directory exists. So, the user has to remove the Ubuntu subsystem directory manually, if they want to re-install the subsystem.

## Limitations
- UBU is being tested on DM 900 with OpenVix image only

## Links
- Installation: https://xcentaurix.github.io/UbuntuCockpit
- Support: https://github.com/xcentaurix/UbuntuCockpit/discussions
