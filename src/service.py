import time

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "$$time$$"+"%.6f" % time.time()+"$$time$$"

# Try to run the application.
try:
	app.run(host='0.0.0.0')
finally:
	print(" * Shutting down our hidden service")
