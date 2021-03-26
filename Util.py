import os
import sys
import json

def AssertDir(directory):
	if not os.path.isdir(directory):
		outString = "**ERROR** Directory " + directory + " does not exist."
		sys.exit(outString)

def SaveJson(directory, filename, source):
	fullPath = directory + '/' + filename
	if os.path.isfile(fullPath):
		outString = " *Error*  File attempting to save: " + fullPath + " already exists."
		print(outString)
	else:
		outString = "Writing file: " + fullPath
		print(outString)
		with open(fullPath, 'w') as outfile:
			json.dump(source, outfile)

def LoadJson(directory, filename, quitOnFail):
	AssertDir(directory)
	fullPath = directory + '/' + filename
	if not os.path.isfile(fullPath):
		outString = " *Error*  File attempting to load: " + fullPath + " does not exist."
		print(outString)
		if quitOnFail:
			sys.exit()
	else:
		outString = "Loading file: " + fullPath
		print(outString)
		with open(fullPath, 'r') as file:
			return json.loads(file.read())

def MakeDir(directory):
	if os.path.isdir(directory):
		outString = "Directory " + directory + " already exists."
	else:
		os.mkdir(directory)
		outString = "Directory " + directory + " created."
	print(outString)

def AppendDateAndTime(timestamp, string):
	return timestamp.strftime("%Y-%m-%d-%H-%M-%S_") + string

def SaveTextFile(directory, filename, source):
	fullPath = directory + '/' + filename
	if os.path.isfile(fullPath):
		outString = " *Error*  File attempting to save: " + fullPath + " already exists."
		print(outString)
	else:
		outString = "Writing file: " + fullPath
		print(outString)
		with open(fullPath, 'w', newline='') as dataOut:
			dataOut.write(source)

def LoadTextFile(directory, filename):
	fullPath = directory + '/' + filename
	if not os.path.isfile(fullPath):
		outString = " *Error*  File attempting to load: " + fullPath + " does not exist."
		print(outString)
		return ''
	else:
		outString = "Loading file: " + fullPath
		print(outString)
		with open(fullPath, 'r') as file:
			return file.read()