from flask import Flask, render_template
from flask_frozen import Freezer
import json, sys

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
	else:
		app.run(debug=True, host="192.168.1.68" )
