# Solem BL-IP Reverse Engineering

https://www.solem.fr/en/residential-watering/9-bl-ip.html


Work in progress:

|Command|Code|Comment|
| --- | --- |---|
|off for x days|3105c0000x0000|set controller off for maximum 15 days (=f)|
|off permanently|3105c000000000|permanently if the number of days is 0| 
|on|3105a000000000|set controller to on|
|transmit|3b00|commit the change
