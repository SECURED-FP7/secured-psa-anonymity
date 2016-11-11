Anonymity PSA: Configuration Update Client
===========================================

To push OpenVpn configuration to PSAR for the Anonymity PSA the push_update.py script should be used. 
The PSAR IP is in the module.conf file along with the PSA ID of the project in PSAR where the configurations will be
pushed and the local path where the OpenVPN configurations are stored. When the script is run it reads each
configuartion file per country, deletes the previous one from PSAR and pushes the new one. For each configuration
file the relative path to the actual file is hardcoded in the country_to_conf dictionary. Thus, in order to use
the script the country_to_conf dictionary must properly point to the configuration file of the country you want
to push to PSAR. Finally, the configurations are encoded in base64 before being pushed to PSAR.

The checkConfigurations.py is used to validate that the configurations have been stored successfuly in PSAR. This
script also uses the same dictionary to point to the local OpenVPN configurations thus it should also be adjusted
as is the case for the push_update.py.