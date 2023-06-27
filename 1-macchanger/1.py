#!/usr/bin/python


import subprocess

interface = input("Interface>  ")
macaddress = input("Mac>  ")


subprocess.call(["sudo","ifconfig",interface,"down"])
subprocess.call(["sudo", "ifconfig",interface,"hw", "ether", macaddress])
subprocess.call(["sudo", "ifconfig",interface,"up"])