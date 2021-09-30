import os
import datetime
import atexit
from Util import SaveTextFile, AppendDateAndTime, MakeDir

def Log_(line):
	logLines.append(line)

def CleanUp_():
	sourceLog = '\n'.join(logLines)
	filenameLog = AppendDateAndTime(datetime.datetime.now(), 'Log') + '.txt'
	SaveTextFile(dirLogs, filenameLog, sourceLog)


os.chdir(os.path.dirname(os.path.abspath(__file__)))
logLines = []
dirLogs = './Logs'
MakeDir(dirLogs)

atexit.register(CleanUp_)
