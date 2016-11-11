'''
This script retrieves configurations for each country from PSAR and
compares it with the local configurations to ensure that they are the same.

It is used as a validity check.


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
    f = open(country_to_conf[location],'r')
    dyn_conf=f.read()
    print 'Configuration for:',location,':'
    dyn_conf = base64.b64encode(dyn_conf)
    print dyn_conf
    f.close()
    
    print 'Getting configuration for:',location,' from PSAR:'
    r=client.get_dyn_conf(psa_id=created_psa_id, location=location)
    data=json.loads(r.text)

    print data['dyn_conf']
    print 'Checking whether retrieved configuration and local configuration are the same:'
    if data['dyn_conf']==dyn_conf:  
        print 'Correct'
    else:
        print 'Not the same'
    print '\n'
    
 
        


