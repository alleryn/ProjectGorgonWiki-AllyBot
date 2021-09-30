import os
import urllib.request
import sys

from Util import LoadTextFile, LoadJson, SaveTextFile, MakeDir
from GlobalStrings import Ab_String, Fv_String, QR_String, QF_String, RU_String, RP_String, RK_String, XP_String

os.chdir(os.path.dirname(os.path.abspath(__file__)))

gameVersion = urllib.request.urlopen('http://client.projectgorgon.com/fileversion.txt').read().decode('UTF-8')
botVersion = LoadTextFile('.', 'BotVersion.txt')
dirBase = './Data/' + botVersion

if not gameVersion == LoadTextFile(dirBase, botVersion + '_GameVersion.txt'):
	sys.exit('**ERROR** GAME VERSION MISMATCH')

dirLoadCompare = dirBase + '/ChangedFiles'
dirLoadWikiData = dirBase + '/WikiData'
dirSave = dirBase + '/VersionizedUploadData'
MakeDir(dirSave)

dirAbSave = dirSave + '/' + Ab_String
dirFvSave = dirSave + '/' + Fv_String
dirQRSave = dirSave + '/' + QR_String
dirQFSave = dirSave + '/' + QF_String
dirRUSave = dirSave + '/' + RU_String
dirRPSave = dirSave + '/' + RP_String
dirRKSave = dirSave + '/' + RK_String
dirXPSave = dirSave + '/' + XP_String
MakeDir(dirAbSave)
MakeDir(dirFvSave)
MakeDir(dirQRSave)
MakeDir(dirQFSave)
MakeDir(dirRUSave)
MakeDir(dirRPSave)
MakeDir(dirRKSave)
MakeDir(dirXPSave)

OtherChangedFiles = LoadJson(dirLoadCompare, 'OtherChangedFiles.json', True)
Changed_Ab_Files = LoadJson(dirLoadCompare, 'Changed_Ab_Files.json', True)
Changed_Fv_Files = LoadJson(dirLoadCompare, 'Changed_Fv_Files.json', True)
Changed_QR_Files = LoadJson(dirLoadCompare, 'Changed_QR_Files.json', True)
Changed_QF_Files = LoadJson(dirLoadCompare, 'Changed_QF_Files.json', True)
Changed_RU_Files = LoadJson(dirLoadCompare, 'Changed_RU_Files.json', True)
Changed_RP_Files = LoadJson(dirLoadCompare, 'Changed_RP_Files.json', True)
Changed_RK_Files = LoadJson(dirLoadCompare, 'Changed_RK_Files.json', True)
Changed_XP_Files = LoadJson(dirLoadCompare, 'Changed_XP_Files.json', True)

for file in OtherChangedFiles:
	SaveTextFile(dirSave, file, LoadTextFile(dirLoadWikiData, file).replace('__GAMEVERSION__', 'v' + gameVersion))
for file in Changed_Ab_Files:
	SaveTextFile(dirAbSave, file, LoadTextFile(dirLoadWikiData + '/' + Ab_String, file).replace('__GAMEVERSION__', 'v' + gameVersion))
for file in Changed_Fv_Files:
	SaveTextFile(dirFvSave, file, LoadTextFile(dirLoadWikiData + '/' + Fv_String, file).replace('__GAMEVERSION__', 'v' + gameVersion))
for file in Changed_QR_Files:
	SaveTextFile(dirQRSave, file, LoadTextFile(dirLoadWikiData + '/' + QR_String, file).replace('__GAMEVERSION__', 'v' + gameVersion))
for file in Changed_QF_Files:
	SaveTextFile(dirQFSave, file, LoadTextFile(dirLoadWikiData + '/' + QF_String, file).replace('__GAMEVERSION__', 'v' + gameVersion))
for file in Changed_RU_Files:
	SaveTextFile(dirRUSave, file, LoadTextFile(dirLoadWikiData + '/' + RU_String, file).replace('__GAMEVERSION__', 'v' + gameVersion))
for file in Changed_RP_Files:
	SaveTextFile(dirRPSave, file, LoadTextFile(dirLoadWikiData + '/' + RP_String, file).replace('__GAMEVERSION__', 'v' + gameVersion))
for file in Changed_RK_Files:
	SaveTextFile(dirRKSave, file, LoadTextFile(dirLoadWikiData + '/' + RK_String, file).replace('__GAMEVERSION__', 'v' + gameVersion))
for file in Changed_XP_Files:
	SaveTextFile(dirXPSave, file, LoadTextFile(dirLoadWikiData + '/' + XP_String, file).replace('__GAMEVERSION__', 'v' + gameVersion))