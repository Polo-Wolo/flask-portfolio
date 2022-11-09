from flask import Flask, render_template
import json
import datetime

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
	
@app.route("/")
def home():
	return render_template("base.html", utc_dt=datetime.datetime.utcnow(), **data, **config)

if __name__ == '__main__':
	app.run(debug=True)
