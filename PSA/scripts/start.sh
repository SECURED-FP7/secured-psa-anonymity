#!/bin/bash
#
# start.sh
#   Created:    19/02/2015
#   Author:     Savvas Charalambides
#
#   Description:
#       Start script for the PSA
#
# This script is called by the PSA API when the PSA is requested to be started.
#
# Load PSA's current configuration

##############################################################
# Initializing OpenVPN tunnel
##############################################################
CONF=/home/psa/pythonScript/psaConfigs/psaconf
AUTH_FILE=/etc/openvpn/authentication.txt
username=$(cat $CONF|sed -n 1p|cut -c 2-)
password=$(cat $CONF|sed -n 2p|cut -c 2-)

echo $username > $AUTH_FILE
echo $password >> $AUTH_FILE

openvpn --config /home/psa/pythonScript/psaConfigs/psaconf &

echo "PSA Started"

exit 1;

