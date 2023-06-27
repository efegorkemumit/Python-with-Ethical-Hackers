#!/usr/bin/python


import subprocess
import optparse




def macchanger(interface, macaddress):
    subprocess.call(["sudo","ifconfig",interface,"down"])
    subprocess.call(["sudo", "ifconfig",interface,"hw", "ether", macaddress])
    subprocess.call(["sudo", "ifconfig",interface,"up"])

    print("Changing mac Adress---->>>" + interface ,  macaddress)


def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="Interface", help="Change the Interface")
    parser.add_option("-m", "--mac", dest="new_mac", help="Change the mac address")
    return parser.parse_args()


(options, arguments) = get_argument()
macchanger(options.Interface, options.new_mac)
