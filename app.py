from flask import Flask, render_template
from flask_frozen import Freezer
import json, sys
import socket
import pathlib


online = 0

if (online):
	# Use to know the server ip in the network
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	ip_addr = s.getsockname()[0]
	s.close()
else:
	ip_addr = "127.0.0.1"

# create a data file
data = {}
# fill it with the json
with open("static/src/json/data.json", 'r') as file:
	data = json.load(file)

# create a config file
config = {}
# fill it with the json
with open("static/src/json/config.json", 'r') as file:
	config = json.load(file)

app = Flask(__name__)
freezer = Freezer(app)

@app.route("/")
def home():
	return render_template("base.html", **data, **config)

if __name__ == '__main__':
	if len(sys.argv) > 1 and sys.argv[1] == "build":
		freezer.freeze()

		cur_dir = str(pathlib.Path(__file__).parent.resolve())

		# Read in the file
		with open(cur_dir+'/build/index.html', 'r') as file :
			filedata = file.read()

		# Replace the target string
		filedata = filedata.replace('href="/static', 'href="../static')
		filedata = filedata.replace('src="../../static', 'src="../static')
		filedata = filedata.replace('src="/static', 'src="../static')
		filedata = filedata.replace('href="../../static', 'href="../static')


		# Write the file out again
		with open(cur_dir+'/build/index.html', 'w') as file:
			file.write(filedata)

	else:
		app.run(debug=True, host=ip_addr )
