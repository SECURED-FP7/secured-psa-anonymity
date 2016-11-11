'''

This script is used to push the local OpenVPN configurations to PSAR.
The path to the configuration is set in the module.conf file. Each configuration file's full path
is stored in the country_to_conf dictionary as shown below. 

The full path to each configuration file is built using the path to the configurations from module.conf
augmented with the relative path to each configuration file. 

'''
from requests import get, put, post, delete
from local_client import Client
import json, hashlib, os
from subprocess import call
import urllib2, base64, ConfigParser


config = ConfigParser.RawConfigParser()
try:
    config.read('module.conf')
    useDefault = False
except:
    print 'Error reading configuration file'

PSAR_URL = config.get('PSAR','psar_ip')

PSAR_URL = os.getenv('PSAR_URL',PSAR_URL)

created_psa_id='anonymity'
path_to_configs = config.get('VPN_CONFS_PATH','confs_path')    
country_to_conf = {}
country_to_conf['cyprus'] = path_to_configs+'/vpncyprus/ptlvpn-cy-tcp443udp1194.ovpn'
country_to_conf['indonesia'] = path_to_configs+'/tcpvpn/id1-tcpvpn.com-443.ovpn'
country_to_conf['singapore'] = path_to_configs+'/tcpvpn/sg1-mct.tcpvpn.com-443.ovpn'
country_to_conf['germany'] = path_to_configs+'/tcpvpn/ge-tcpvpn.com-443.ovpn'
country_to_conf['usa'] = path_to_configs+'/vpnbook/vpnbook-us1-tcp443.ovpn'
country_to_conf['romania'] = path_to_configs+'/vpnbook/vpnbook-euro1-tcp443.ovpn'
country_to_conf['france'] = path_to_configs+'/vpnme/vpnme_fr_tcp443.ovpn'
country_to_conf['uk'] = path_to_configs+'/vpnkeys/uk1.vpnkeys.com.tcp.ovpn'

client=Client(PSAR_URL)

for location in country_to_conf:
    '''
    Reading the configuration file and encoding it in base64.
    '''
    f = open(country_to_conf[location],'r')
    dyn_conf=f.read()
    dyn_conf = base64.b64encode(dyn_conf)
    print dyn_conf
    f.close()
    
    '''
    Removing previous configuration from PSAR.
    '''
    print 'Trying to delete configuration for:',location
    r=client.delete_dyn_conf(psa_id=created_psa_id, location=location)
    if (r.status_code==204):
        print 'Deleted configuration for ',location
    else:
        print 'Did not delete configuration for ',location, ' returned with status:',str(r.status_code)
    
    '''
    Pushing configuration to PSAR
    '''
    print 'Trying to push configuration for:',location
    r=client.put_dyn_conf(psa_id=created_psa_id, location=location, dyn_conf=dyn_conf)
    if r.status_code==201:
        print 'Pushed configuration for ',location
    else:
        print 'Did not push configuration for ',location, ' returned with status:',str(r.status_code)
        
    print '\n'        
        