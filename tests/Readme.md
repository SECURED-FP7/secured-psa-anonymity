Testing Methodology
---

1. In order to test the Anonymity PSA using the local NED account first configure the local NED to suport the anon using the [NED Files](NED Files). Also you have to add the anon account in the userList of the local NED.
2. After appropriately configuring the local NED you have to overwrite the psa configuration([anonymity](NED Files/psaConfigs/anonymity/anonymity)) in order to connect to one of the following countries:
    * [Cyprus](tests/OpenVPN Remote Server Configurations/vpncyprus/ptlvpn-cy-tcp443udp1194.ovpn)
    * [USA](tests/OpenVPN Remote Server Configurations/vpnbook/vpnbook-ca1-tcp443.ovpn)
    * [USA2](tests/OpenVPN Remote Server Configurations/vpnbook/vpnbook-us1-tcp443.ovpn)
    * [Germany](tests/OpenVPN Remote Server Configurations/vpnbook/vpnbook-de233-tcp443.ovpn)
    * [Romania](tests/OpenVPN Remote Server Configurations/vpnbook/vpnbook-euro1-tcp443.ovpn)
    * [Romania2](tests/OpenVPN Remote Server Configurations/vpnbook/vpnbook-euro2-tcp443.ovpn)
    * [UK](tests/OpenVPN Remote Server Configurations/vpnkeys/uk1.vpnkeys.com.tcp.ovpn )
    * [France](tests/OpenVPN Remote Server Configurations/vpnme/vpnme_fr_tcp443.ovpn)
    * [Singapore](tests/OpenVPN Remote Server Configurations/tcpvpn/sg1-mct.tcpvpn.com-443.ovpn)
    * [Indonesia](tests/OpenVPN Remote Server Configurations/tcpvpn/id1-tcpvpn.com-443.ovpn )
3. The above configuration files are ready-to-use. Namely, you can emulate the HSPL selection of country by using one of the files above and overwriting the configuration file in TVDM/psaConfigs/anonymity/.
4. After choosing the appropriate configuration file you want to test, use the anon account and log-into the NED.
5. After PSA starts the OpenVPN tunnel will be deployed. Tests indicate that after ~25 seconds from logging in the PSA should be up and the tunnel should also be set-up.
6. Finally you can visit the following sites to make sure that your identity is now forged:
    * http://mylocation.org/
    * https://www.whatismyip.com/
