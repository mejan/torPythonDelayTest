import socket
import socks
import time
import sys

# Setting up socks5 for proxy.
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
s = socks.socksocket()

file = open('measurements/url.txt','r')

# Connect to the "Tor" service.
s.connect((file.read()+".onion", 80))
file.close()

# Message to the hidden service.
message = "GET / HTTP/1.1\r\n\r\n"
# try to send request.
try:
	s.send(message)
except socket.error:
	print "send failed"
	sys.exit()
print "Message sent: success.\n"

# Function to revice data.
def recvDataTimeout(zeSocket, timeout=2):
	#Make non-blocking
	zeSocket.setblocking(0)

	# totData has all the data as an array and data used to tmp store the data
	totData=[]
	# data is used to temporarlly store the recived data.
	data=""
	# tmp is to store time stamp for when the wanted data is recived
	tmp=0.0

	#begin time for measure if timeout.
	begin=time.time()
	while 1:
		# If we recive data close after timeout period.
		if totData and time.time()-begin > timeout:
			break
		# If no data is recived wait twice as long
		elif time.time()-begin > 2*timeout:
			break

		#recv data
		try:
			data = zeSocket.recv(2048)
			if data:
				totData.append(data)
				# if to see when we recive the data we want.
				if "$$time$$" in data:
					tmp = float("%.6f" % time.time())
				# change begin time for "reseting" the timeout.
				begin=time.time()
			else:
				# sleep a bit.
				time.sleep(0.1)
		except:
			pass
	# join the totData to one string that is returned.
	return tmp, "".join(totData)

# Capture the return data from recvData... function.
recivedTime, message = recvDataTimeout(s)

# Sliting the recived message.
splitedMessage = message.split("$$time$$")
sentTime = float(splitedMessage[1])

# Print the data.
print repr(recivedTime-sentTime)+" s, to send the message in the TOR network."

# Save the recived delayed to file (appended).
file = open('measurements/reciveDelayTor.txt', 'a')
file.write(repr(recivedTime-sentTime)+" s\n\n")
file.close()