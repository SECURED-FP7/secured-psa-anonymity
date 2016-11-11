#!/bin/bash
#
# stop.sh
#   Created:    19/02/2015
#   Author:     Savvas Charalambides
#
#   Description:
#       This script closes the OpenVPN tunnel and clear the configuration environmet.
#
# This script is called by the PSA API when the PSA is requested to be stopped.
#


# Flush iptables
iptables -F
iptables -X
iptables -t nat -F
iptables -t nat -X
iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT


ip route flush table 100
ip rule del fwmark 1 lookup 100

echo "flushing any exiting rules"
iptables -t mangle -F
iptables -t mangle -X DIVERT

echo "flushing routing cache"
ip route flush cache

##########################################################
echo "flusing ebtables"
ebtables -F
ebtables -X
for T in filter nat broute; do   ebtables -t $T -F;   ebtables -t $T -X; done
ebtables -P INPUT ACCEPT
ebtables -P FORWARD ACCEPT
ebtables -P OUTPUT ACCEPT

echo "stopping openvpn"
ifconfig tun0 down

echo "PSA Stopped"
exit 1;

