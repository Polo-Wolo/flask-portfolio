from flask import Flask, render_template
from flask_frozen import Freezer
import json, sys, socket, pathlib, os, shutil



if (len(sys.argv) > 1 and sys.argv[1]=="host"):
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

def changeRelativePath():
	# get current directory path
	cur_dir = str(pathlib.Path(__file__).parent.resolve())

	# Read in the file
	with open(cur_dir+'/build/index.html', 'r') as file :
		filedata = file.read()

	# Replace the target string
	filedata = filedata.replace('href="/static', 'href="static')
	filedata = filedata.replace('src="../../static', 'src="static')
	filedata = filedata.replace('src="/static', 'src="static')
	filedata = filedata.replace('href="../../static', 'href="static')
	print("Relative paths changed !")


	# Write the file out again
	with open(cur_dir+'/build/index.html', 'w') as file:
		file.write(filedata)

def cleanFiles(rltv_src_dir, rltv_dst_dir):
	# get current directory path
	cur_dir = str(pathlib.Path(__file__).parent.resolve())

	# Cleaning directory for gh host
	for files in os.listdir(cur_dir):
		path = os.path.join(cur_dir, files)
		#print(path)
		if(path!=(cur_dir+'/build') and path!=(cur_dir+'/README.md') and path!=(cur_dir+'/.gitignore') and path!=(cur_dir+'/.git')):
			try:
				shutil.rmtree(path)
			except OSError:
				os.remove(path)
	
	# move everyfiles from build to current directory
	src = cur_dir+rltv_src_dir
	dst = cur_dir+rltv_dst_dir
	print("src : "+src)
	print("dst : "+dst)
	
	# Iterate through the list of items
	for item in os.listdir(src):
		# Construct the source and destination file paths
		source_item = os.path.join(src, item)
		dest_item = os.path.join(dst, item)
		
		# Move the item from the source to the destination
		shutil.move(source_item, dest_item)

	#remove build folder
	try:
		shutil.rmtree(cur_dir+'/build')
	except OSError:
		os.remove(cur_dir+'/build')

if __name__ == '__main__':
	if (len(sys.argv) > 1 and sys.argv[1] == "build"):
		freezer.freeze()

		changeRelativePath()
		cleanFiles(rltv_src_dir='/build',rltv_dst_dir='')
		print("Build done !")

	else:
		app.run(debug=True, host=ip_addr)
