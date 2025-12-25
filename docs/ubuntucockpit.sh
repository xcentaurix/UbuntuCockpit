#!/bin/sh
rm -f /etc/opkg/cockpit-feed.conf
opkg update
src/gz cockpit https://xcentaurix.github.io/Cockpit-Feed/packages/armhf > /etc/opkg/cockpit-feed-armhf.conf
opkg update
opkg install enigma2-plugin-systemplugins-ubuntucockpit
init 2
init 3
