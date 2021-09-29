import os
import datetime

from Util import MakeDir, AppendDateAndTime, LoadTextFile, SaveTextFile

def GetLatestBackup(filename):
	backups = sorted([f for f in os.listdir('./Backups') if f.endswith(filename)], reverse=True)
	if backups:
		return LoadTextFile('./Backups', backups[0])
	else:
		return None

def BackupPyFiles(timestamp, directory):
	files = set(f for f in os.listdir(directory) if f.endswith('.py'))
	for filename in files:
		source = LoadTextFile(directory, filename)
		if not source == GetLatestBackup(filename):
			SaveTextFile('./Backups', AppendDateAndTime(timestamp, filename), source)
			print('Saving backup to ' + filename)


os.chdir(os.path.dirname(os.path.abspath(__file__)))

MakeDir('./Backups')

timestampBackup = datetime.datetime.now()
BackupPyFiles(timestampBackup, '.')
BackupPyFiles(timestampBackup, './Generators')
