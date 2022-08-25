import clipboard
import sys
import json

Help = """
Usage:
python multiclipboard.py save // To save data from the clipboard to a MultiClipBoard.json
python multiclipboard.py load // To load data from the MultiClipBoard.json to clipboard
python multiclipboard.py list // To view all the data stored in MultiClipBoard.json
"""


MultiClipBoard = "MultiClipBoard.json"

def save_data(file, data):
	with open(file, "w") as f:
		json.dump(data,f)

def load_data(file):
	try:
		with open(file, "r") as f:
			data = json.load(f)
			return data
	except:
		return {}

args = list(sys.argv)

if args[1] == "-help":
	print(Help)

if len(args) == 2:
	cmd = args[1]
	data = load_data(MultiClipBoard)
	
	if(cmd == "save"):
		key = input("Enter a key: ")
		data[key] = clipboard.paste()
		save_data(MultiClipBoard, data)
		print("Data Saved")
	elif(cmd == "load"):
		key = input("Enter a key: ")
		if key in data:
			clipboard.copy(data[key])
			print("Data copied to clipboard....")
		else:
			print("Key doesn't exisit")
	elif(cmd == "list"):
		print(data)
	elif(cmd != "-help"):
		print("Unknown Command")
		print(Help)

