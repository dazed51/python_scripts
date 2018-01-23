#!/usr/bin/python3

#script to connect to vpn
#recipe: modules - os, sys
#open file, eval privledge, set process in background, execute command, verify masked ip

import sys, time
import subprocess
from requests  import get
from pathlib import Path

#verify if vpn file exists

ovpn = Path("/home/xtify/client1.ovpn")
if ovpn.is_file():
    print ("ovpn file found proceeding.." "\n")
    time.sleep(3)
else:
    print ("ovpn file not found" "\n")

def vpnconnect():
    print("executing vpn connect script" "\n")
    time.sleep(3)
    subprocess.Popen("openvpn --config client1.ovpn", shell=True)
vpnconnect()

def getpub():
    time.sleep(6)
    #making request to get public ip address
    ip = get('https://api.ipify.org').text
    print ('public ip after connecting to vpn is now: {}'.format(ip))
getpub()
