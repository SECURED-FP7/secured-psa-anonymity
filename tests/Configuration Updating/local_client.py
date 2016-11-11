#!/usr/bin/python

from requests import get, put, delete, patch, post
import urllib
import argparse,json, os

'''
Client for the PSAR API. All methods return a Response object.

TO-DO: Currently only tested without authentication. 
'''

    
class Client:
    def __init__(self,base_url):
        self.base_url=base_url+'/v1/'

    #dyn_conf
    def put_dyn_conf(self, psa_id, location, dyn_conf, token=None):
        url=self.base_url+'PSA/dyn_conf/'+psa_id+'/'
        params={}
        if token: 
            params['token']=token
        params['location']=location
        params['dyn_conf']=dyn_conf
        return put(url, params=params)

    def get_dyn_conf(self, psa_id, location, token=None):
        url= self.base_url+'PSA/dyn_conf/'+psa_id+'/?location='+location
#         print 'Sending URL:'+url
        params={}
        if token:
                params['token']=token
        params['location']=location
        return get(url, params=params)

    def delete_dyn_conf(self, psa_id, location, token=None):
        url= self.base_url+'PSA/dyn_conf/'+psa_id
        params={}
        if token:
                params['token']=token
        params['location']=location
        return delete(url, params=params)





