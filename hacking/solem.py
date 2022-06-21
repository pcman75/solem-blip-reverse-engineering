import struct
import binascii
from bluepy import btle


'''
Identified commands
--------------------------------
off permanently | 3105c000000000
off today       | 3105c000010000
off 2 days      | 3105c000020000
...             |
off 15 days:    | 3105c0000f0000
--------------------------------
on:             | 3105a000000000
--------------------------------
all stations XXXX seconds | 3105110000XXXX | XXXX: number of seconds, max 0xa8c0 = 12h
--------------------------------
31051400010000 dimi seara
31051400020000 avarie


3105120100012c spate 5 min
3105120200012c fata 5 min
3105120300012c intrare 5 min
31051203000268 intrare 10 min
stop manual:    | 31051500ff0000
--------------------------------
transmit:       | 3b00
'''

class BLIPNotification(btle.DefaultDelegate):
    def __init__(self, params):
        btle.DefaultDelegate.__init__(self)
        print(f"Created delegate for handle {params}")
        # ... initialise here

    def handleNotification(self, cHandle, data):       
        # ... perhaps check cHandle
        # ... process 'data'
        btle.DefaultDelegate.__init__(self)       
        print(f"Notification from {cHandle}: {binascii.hexlify(data)} {data}")

def handleNotifications(per, wait):
    while wait:
        if per.waitForNotifications(1.0):
            # handleNotification() was called
            continue
        print("Waiting...")
        wait = wait - 1

per = btle.Peripheral()

#C8:B9:61:06:69:96
try:
    bytes = b'0x00'
    per = btle.Peripheral("C8:B9:61:06:69:96", btle.ADDR_TYPE_RANDOM)
    

    characteristics = per.getCharacteristics()    
    for characteristic in characteristics:
        print("{}, hnd={}, supports {}".format(characteristic, hex(characteristic.handle), characteristic.propertiesToString()))
        #if characteristic.uuid == '00002a04-0000-1000-8000-00805f9b34fb':
        #    bytes = characteristic.read()
        #    print("Read {}", struct.unpack('BBBBBBH', bytes))

        if characteristic.uuid == '108b0002-eab5-bc09-d0ea-0b8f467ce8ee':
            characteristicWrite = characteristic

        elif characteristic.uuid == '108b0003-eab5-bc09-d0ea-0b8f467ce8ee':
            characteristicNotify = characteristic

    per.setDelegate(BLIPNotification(characteristicNotify.getHandle()))

    # Setup to turn notifications on, e.g.
    per.writeCharacteristic(characteristicNotify.getHandle()+1, b"\x01\x00")
    
    
    #0x31051201000294 - stop any manual watering program
    print("writing command")
    characteristicWrite.write(struct.pack(">HBBBH",0x3105,0x12,0x01,0x00,0x0294))
    handleNotifications(per, 1)
    print("committing")
    characteristicWrite.write(struct.pack(">BB",0x3b,0x00))
    handleNotifications(per, 1)
    
except btle.BTLEException as e:
    print("BLE Exception:", e)

finally:
    per.disconnect() 


""" 
characteristics = dev.getCharacteristics()
print("Got",len(characteristics),"characteristic objects")

for characteristic in characteristics:
    print("{}, hnd={}, supports {}".format(characteristic, hex(characteristic.handle), characteristic.propertiesToString()))
    print('uuid = {}', characteristic.uuid)
    if characteristic.uuid == '00002a04-0000-1000-8000-00805f9b34fb':
        bytes = characteristic.read()
        #test = struct.unpack('BBBBBB', bytes)
        print("Read {}", bytes)
"""

