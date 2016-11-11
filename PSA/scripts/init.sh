#!/bin/bash
#
#	Date: 19/02/2016
#	Author: Savvas Charalambides
#
#	This script handles the forwarding of all traffic
#	via the OpenVPN tunnel.
#/////////////////////////////////////////////////////////
sysctl -w net.ipv4.ip_forward=1
sysctl -p

ebtables -t broute --flush
iptables -t nat --flush

## interface facing clients
CLIENT_IFACE=eth0

## interface facing Internet
INET_IFACE=eth1

ebtables -P FORWARD DROP
ebtables -A FORWARD -p IPv4 -j ACCEPT
ebtables -A FORWARD -p ARP -j ACCEPT
ebtables -t broute -A BROUTING -i $CLIENT_IFACE -p ipv4 -j redirect --redirect-target DROP
ebtables -t broute -A BROUTING -i $INET_IFACE -p ipv4 -j redirect --redirect-target DROP

#ebtables -t nat -A PREROUTING --logical-in br0 -p ipv4 --ip-protocol 6 -j redirect --redirect-target ACCEPT
#ebtables -t nat -A PREROUTING --logical-in br0 -p ipv4 --ip-protocol 6 -j redirect --redirect-target ACCEPT


# Allow postrouting to tun0.
iptables -t nat -A POSTROUTING -o tun0  -j MASQUERADE

# Enable forwarding from the LAN to the VPN (and back via related and established connections).
iptables -A FORWARD -i br0 -o tun0 -j ACCEPT
iptables -A FORWARD -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT

#iptables -t nat -A POSTROUTING --out-interface tun0 -j MASQUERADE


exit 1;
