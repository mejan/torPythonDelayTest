# SchoolProject delay TOR

This is an test enviorment for measuring delay's for a school course.

## Requirements
python 2.7.12 (might work with lower).


### import (some of is serpertly installed)
* stem - python module for TOR (The onion routing).<br />
* SocksiPy - python module for connection through a SOCKS proxy server<br />
 + Socks - part of SocksiPy<br />
* Socket - This module provides access to the BSD socket interface.<br />
* requests - Non-GMO HTTP libary for python<br />
* time - module for accessing diffrent time on the computer (the computer clock for example)<br />
* sys - to interact with the interpriter<br />
* shutil - for high level file operations<br />
* os - module for portably use operative system dependent functionality<br />
* flask - for webdeveloping in python.

#### Not required but recommened
This is not a required application but I strongly suggest the use of pip for installing<br />
sepertly installed imports.

### Donot forget

Do not forget to set ControlPort and hasdedpassword in the torrc file (in my system its located in /etc/tor/torrc).

## Start procedure
change directory into toCode, well in there do the following:
open a terminal window and run:
```
sudo bash runScript.bash
```
then open an other terminal window and run:
```
tshark -i any -a duration:604910 -w packetCaptured.pcapng
```
This will take about one week to finish, so let it run.

## Disclaimer
Just because it uses tor doesn't garanti it's totaly anonymous, it also depends on implementation. because this is implmentated just for delay testing no anonymity is not garantied.

You may use the code as you see fit but this is done your own risk. Nothing is supported and no garanti is given.

## Author
Only one author: mejan mifa1100@student.miun.se.
