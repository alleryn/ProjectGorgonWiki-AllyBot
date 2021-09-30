import os
import sys
import urllib.request
from Util import LoadTextFile,MakeDir, SaveJson
from GlobalStrings import Ab_String, Fv_String, QR_String, QF_String, RU_String, RP_String, RK_String, XP_String

def FindChangedFiles(directory):
	dirCurrent = dirBaseCurrent + '/' + directory
	dirPrevious = dirBasePrevious + '/' + directory
	changedFiles = []

	files = set(f for f in os.listdir(dirCurrent) if f.endswith('.txt'))
	for file in files:
		if not LoadTextFile(dirCurrent, file) == LoadTextFile(dirPrevious, botVersionPrevious + file[3:]):
			changedFiles.append(file)
	return changedFiles


os.chdir(os.path.dirname(os.path.abspath(__file__)))

gameVersion = urllib.request.urlopen('http://client.projectgorgon.com/fileversion.txt').read().decode('UTF-8')

botVersionCurrent = LoadTextFile('.', 'BotVersion.txt')
dirBaseCurrent = './Data/' + botVersionCurrent
dirLoadCurrent = dirBaseCurrent + '/WikiData'
if not gameVersion == LoadTextFile(dirBaseCurrent, botVersionCurrent + '_GameVersion.txt'):
	sys.exit('**ERROR** GAME VERSION MISMATCH')

botVersionPrevious = str(int(botVersionCurrent) - 1)
dirBasePrevious = './Data/' + botVersionPrevious
dirLoadPrevious = dirBasePrevious + '/WikiData'

dirSave = dirBaseCurrent + '/ChangedFiles'
MakeDir(dirSave)
SaveJson(dirSave, 'OtherChangedFiles.json', FindChangedFiles('WikiData'))
SaveJson(dirSave, 'Changed_Ab_Files.json', FindChangedFiles('WikiData/' + Ab_String))
SaveJson(dirSave, 'Changed_Fv_Files.json', FindChangedFiles('WikiData/' + Fv_String))
SaveJson(dirSave, 'Changed_QR_Files.json', FindChangedFiles('WikiData/' + QR_String))
SaveJson(dirSave, 'Changed_QF_Files.json', FindChangedFiles('WikiData/' + QF_String))
SaveJson(dirSave, 'Changed_RU_Files.json', FindChangedFiles('WikiData/' + RU_String))
SaveJson(dirSave, 'Changed_RP_Files.json', FindChangedFiles('WikiData/' + RP_String))
SaveJson(dirSave, 'Changed_RK_Files.json', FindChangedFiles('WikiData/' + RK_String))
SaveJson(dirSave, 'Changed_XP_Files.json', FindChangedFiles('WikiData/' + XP_String))