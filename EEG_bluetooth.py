##pip install pybluez
## pip install numpy

import bluetooth
import socket
import numpy

def print_info_device(device):
    print('\n')
    print('Device:')
    print('Device Name: %s' % device[1])
    print('Device MAC Address: %s' % device[0])
    print('Device Class: %s' % device[2])


def scan(name):
    devices = bluetooth.discover_devices(lookup_names = True, lookup_class = True, flush_cache = True)
    try:
        brain = [device for device in devices if device[1] == name][0]
        print_info_device(brain)
        return brain[0]
    except:
        print('BrainLink_Lite Not found:')
        for device in devices:
            print_info_device(device)


brain = scan('BrainLink_Lite')


#############
 
port = 1
 
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((brain, port))


data_raw = sock.recv(15)
bytes_ = [ord(data_raw[x]) for x in range(len(data_raw))] 


for i in range(10):
    data_raw = sock.recv(15)
    bytes_ = [ord(data_raw[x]) for x in range(len(data_raw))] 
    bytes_









