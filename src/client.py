import requests
import time

# Need to change to the right IP-adress.
r=requests.get('http://ipAddressToServer:5000')
recivedTime = float("%.6f" % time.time())

file = open('measurements/reciveDelay.txt', 'a')
file.write(repr(recivedTime-float(r.text.split("$$time$$")[1]))+" s\n\n")
file.close()
