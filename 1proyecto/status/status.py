#!/usr/bin/env python

import requests
import sys

host = '172.17.0.3:8000'

if len(sys.argv) > 1:
    hito = sys.argv[1]
else:
    hito = None

if hito == None:
    r=requests.get('http://'+host+'/status')
else:
    r=requests.get('http://'+host+'/hito/'+hito)

print(r.status_code, "\n", r.text)
