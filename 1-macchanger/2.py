#!/usr/bin/python


import subprocess
import optparse

parser= optparse.OptionParser()

parser.add_option("-i", "--interface", dest="Interface", help="Change the Interface")
parser.add_option("-m", "--mac", dest="new_mac", help="Change the mac address")

(options, arguments) = parser.parse_args()

interface = options.Interface
macaddress = options.new_mac


subprocess.call(["sudo","ifconfig",interface,"down"])
subprocess.call(["sudo", "ifconfig",interface,"hw", "ether", macaddress])
subprocess.call(["sudo", "ifconfig",interface,"up"])

print("Changing mac Adress---->>>" + interface ,  macaddress)