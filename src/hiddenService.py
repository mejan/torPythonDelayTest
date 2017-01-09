import os
import shutil
import time

from stem.control import Controller
from flask import Flask

app = Flask(__name__)


# This is what will be shown on the hidden service.
@app.route('/')
def index():
	return "$$time$$"+"%.6f" % time.time()+"$$time$$"

# Message to the user that the script is trying to connect.
print(' * Connecting to tor')
start = time.time()
# changing the controller.form_port() to controller as "name"
with Controller.from_port() as controller:
	controller.authenticate("negerDase")

	# All hidden services have a directory on disk. Lets put ours in tor's data
	# directory.

	hidden_service_dir = os.path.join(controller.get_conf('DataDirectory', '/tmp'), 'hello_world')

	# Create a hidden service where visitors of port 80 get redirected to local
	# port 5000 (this is where Flask runs by default).

	response = controller.create_ephemeral_hidden_service({80: 5000}, await_publication = True)
	end = time.time()
	
	# Write URL to file.
	file = open('measurements/url.txt', 'w')
	file.write(""+response.service_id)
	file.close()

	# Append startup delay to file.
	file = open('measurements/startUpDelay.txt', 'a')
	timeDelta=end-start
	file.write(repr(timeDelta)+" s\n\n")
	file.close()

	# Just printing for helping development.
	print(" * Our service is available at %s.onion, press ctrl+c to quit" % response.service_id+".onion")
	print(" * Created hidden service in %s" % hidden_service_dir)

	# Try to run the application.
	try:
		app.run()
	finally:
		print(" * Shutting down our hidden service")