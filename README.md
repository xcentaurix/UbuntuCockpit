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

## Disclaimer
The project author is not responsible for how this software is used by others. It is not intended to be used for accessing or distributing copyrighted materials without authorization.
Users are solely responsible for determining the legality of their actions.

This repository has no control over the streams, links, or the legality of the content provided by the different hosts (including all mirror sites). It is the end user's responsibility to ensure the legal use of these streams, and we strongly recommend verifying that the content complies with all applicable laws, including copyright laws and regulations of your country's jurisdiction before use.

## Limitations
- Tested on OpenViX and OpenATV with DM900.

## Links
- Installation: https://xcentaurix.github.io/UbuntuCockpit
