import json

def Load(path): # Open the settings.json file and parse it
	with open(path, "r") as f:
		return json.loads(f.read())
