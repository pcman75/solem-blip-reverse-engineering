# Solem BL-IP Reverse Engineering

https://www.solem.fr/en/residential-watering/9-bl-ip.html


# Manual control

|Command|Code|Comment|
| --- | --- |---|
**On/Off**
|on|3105a000000000|set controller to on|
|off for X days|3105c0000x0000|set controller off for maximum 15 days (=f)|
|off permanently|3105c000000000|permanently if the number of days is 0|
**Manual Control by Stations**
|all stations for XXXX seconds|3105110000XXXX|XXXX: number of seconds, max 0xa8c0 = 12h|
|station X for YYYY seconds|310514000XYYYY|TODO: test this|
|station X for programmed time|310514000X0000||
**Manual Control by Programs**
|run program X|3105120X000000|
**Stop**
stop in-progress watering|31051500ff0000
**Commit**
|Commit|3b00|commit the manual command
