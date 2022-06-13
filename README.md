# Solem BL-IP irrigation controller bluetooth protocol - documentation

https://www.solem.fr/en/residential-watering/9-bl-ip.html

Tested on model with 4 stations. Controller Software version: **5.1.5**

# How to control via bluetooth
Write the command to the characteristic ```108b0002-eab5-bc09-d0ea-0b8f467ce8ee``` followed by writing 3b00 to the same characteristic

# Commands discovered
|Command|Code|Comment|
| --- | --- |---|
**On/Off**
|on|3105a000000000|set controller to on|
|off for X days|3105c0000x0000|set controller off for maximum 15 days (=f)|
|off permanently|3105c000000000|permanently if the number of days is 0|
**Manual Control by Stations**
|all stations for XXXX seconds|3105110000XXXX|XXXX: number of seconds, max 0xa8c0 = 12h|
|station X for YYYY seconds|3105120X00YYYY
**Manual Control by Programs**
|run program X for the programmed time|310514000X0000
**Stop**
stop in-progress watering|31051500ff0000
**Commit**
|Commit|3b00|commit the manual command



# Samples

bluepy sample snippets:

```
# Assumming characteristicWrite is the characteristic with uuid '108b0002-eab5-bc09-d0ea-0b8f467ce8ee'

#3105-a0-00000000 - turn on the controller
print("writing command")
characteristicWrite.write(struct.pack(">HBBBH",0x3105,0xa0,0x00,0x01,0x0000))
print("committing")
characteristicWrite.write(struct.pack(">BB",0x3b,0x00))

#3105-c0-0003-0000 - 3 days off
print("writing command")
characteristicWrite.write(struct.pack(">HBBBH",0x3105,0xc0,0x00,0x03,0x0000))
print("committing")
characteristicWrite.write(struct.pack(">BB",0x3b,0x00))

#3105-c0-0000-0000 - off permanently
print("writing command")
characteristicWrite.write(struct.pack(">HBBBH",0x3105,0xc0,0x00,0x00,0x0000))
print("committing")
characteristicWrite.write(struct.pack(">BB",0x3b,0x00))

#3105-11-0000-XXXX - all stations 7 min
print("writing command")
characteristicWrite.write(struct.pack(">HBBBH",0x3105,0x11,0x00,0x00,0x6270))
print("committing")
characteristicWrite.write(struct.pack(">BB",0x3b,0x00))

#3105-12-03-00-0294 - station 3 for 11 minutes
print("writing command")
characteristicWrite.write(struct.pack(">HBBBH",0x3105,0x12,0x03,0x00,0x0294))
print("committing")
characteristicWrite.write(struct.pack(">BB",0x3b,0x00))

#3105-15-00-ff-0000 - stop any manual watering program
print("writing command")
characteristicWrite.write(struct.pack(">HBBBH",0x3105,0x15,0x00,0xff,0x0000))
print("committing")
characteristicWrite.write(struct.pack(">BB",0x3b,0x00))
```
# Contribution
Test on your controller and confirm if it's working perhaps on a different controller model with a different programming
