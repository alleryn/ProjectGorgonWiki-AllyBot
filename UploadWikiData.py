import os
import urllib.request
import sys
import requests
from Util import LoadTextFile, SaveTextFile, MakeDir, LoadJson
import Logger
from GlobalStrings import Ab_String, Fv_String, QR_String, QF_String, RU_String, RP_String, RK_String, XP_String

def main(*args):
	logString = 'UploadWikiData.py: '

	def log(line):
		Logger.Log_(logString + line)

	def getSectionNumber(page_, sectionName_):
		PARAMS_ = {"action": "parse", "page": page_, "prop": 'sections', "format": 'json'}
		R_ = S.get(url=URL, params=PARAMS_)
		DATA_ = R_.json()
		sectionList_ = []
		if 'parse' in DATA_ and 'sections' in DATA_['parse']:
			sections_ = DATA_['parse']['sections']
			for section_ in sections_:
				if section_["anchor"] == sectionName_:
					sectionList_.append(section_["index"])
		if len(sectionList_) == 1:
			return sectionList_[0]
		elif len(sectionList_) == 0:
			return -1
		else:
			outputString_ = "**ERROR**: cannot find section number for " + page_ + '#' + sectionName_ + '.'
			print(outputString_)
			log(outputString_)
			return None

	def editSection(page_, section_, sectionNumber_, sectionText_, summary_):
		PARAMS_EditPage_ = {"action": "edit", "format": 'json', "text": sectionText_, "title": page_, "section": sectionNumber_, "summary": summary_, "bot": '1', "token": CSRF_TOKEN}
		log('Editing ' + page_ + '#' + section_)
		R_ = S.post(URL, data=PARAMS_EditPage_)
		DATA_ = R_.json()

		if "edit" in DATA_ and "result" in DATA_["edit"] and "Success" == DATA_["edit"]["result"]:
			with open(completedSectionsFullPath, 'a', newline='') as dataOut_:
				dataOut_.write(page_ + '#' + section_ + '\n')
		else:
			outString_ = 'Failed ' + ' to edit ' + page_ + '#' + section_
			print(outString_)
			print(DATA_)
			log(outString_)
			log(DATA_)
			sys.exit()

	def editPage(page_, text_, summary_):
		PARAMS_EditPage_ = {"action": "edit", "format": 'json', "text": text_, "title": page_, "summary": summary_, "bot": '1', "token": CSRF_TOKEN}
		log('Editing ' + page_)
		R_ = S.post(URL, data=PARAMS_EditPage_)
		DATA_ = R_.json()

		if "edit" in DATA_ and "result" in DATA_["edit"] and "Success" == DATA_["edit"]["result"]:
			with open(completedSectionsFullPath, 'a', newline='') as dataOut_:
				dataOut_.write(page_ + '\n')
		else:
			outString_ = 'Failed ' + ' to edit ' + page_
			print(outString_)
			print(DATA_)
			log(outString_)
			log(DATA_)
			sys.exit()

	def UploadSectionForEachItemPage(sectionName, dirSection):
		for f_ in os.listdir(dirSection):
			if f_.endswith('.txt'):
				page_ = ItemDict[f_[7:-4]]["Page"]
				section_ = sectionName
				if not page_ + '#' + section_ in completedPageSectionPairs:
					sectionNumber_ = getSectionNumber(page_, section_)
					if sectionNumber_ is not None and not sectionNumber_ == -1:
						sectionText_ = LoadTextFile(dirSection, f_)
						summary_ = '/* ' + section_ + ' */ Bot added info for game version v' + gameVersion + ', bot version ' + botVersion + '. Contact [[User:Alleryn]] for issues concerning this bot edit.'
						editSection(page_, section_, sectionNumber_, sectionText_, summary_)
					else:
						outputString_ = "**ERROR**: cannot find section number for " + page_ + '#' + section_ + '.'
						print(outputString_)
						log(outputString_)

	def ArchivePyFiles(directory):
		files = set(f_ for f_ in os.listdir(directory) if f_.endswith('.py'))
		for filename in files:
			source = LoadTextFile(directory, filename)
			SaveTextFile(dirPython, botVersion + '_' + filename, source)

	os.chdir(os.path.dirname(os.path.abspath(__file__)))
	gameVersion = urllib.request.urlopen('http://client.projectgorgon.com/fileversion.txt').read().decode('UTF-8')
	botVersion = LoadTextFile('.', 'BotVersion.txt')
	dirBase = './Data/' + botVersion
	if not gameVersion == LoadTextFile(dirBase, botVersion + '_GameVersion.txt'):
		outputString = '**ERROR** GAME VERSION MISMATCH'
		log(outputString)
		sys.exit(outputString)

	S = requests.Session()
	URL = "http://wiki.projectgorgon.com/w/api.php"

	PARAMS_GetLoginToken = {"action": "query", "meta": 'tokens', "type": 'login', "format": 'json'}
	log('Getting logintoken')
	R = S.get(url=URL, params=PARAMS_GetLoginToken)
	DATA = R.json()
	LOGIN_TOKEN = DATA['query']['tokens']['logintoken']
	if not LOGIN_TOKEN:
		sys.exit("Login Token acquisition failed!")

	PARAMS_DoLogin = {"action": "login", "lgname": sys.argv[1], "lgpassword": sys.argv[2], "lgtoken": LOGIN_TOKEN, "format": 'json'}
	log('Logging in')
	R = S.post(URL, data=PARAMS_DoLogin)
	DATA = R.json()
	if not DATA['login']['result'] == "Success":
		sys.exit("Login failed!")

	PARAMS_GetCsrfToken = {"action": "query", "meta": 'tokens', "format": 'json'}
	log('Getting csrftoken')
	R = S.get(url=URL, params=PARAMS_GetCsrfToken)
	DATA = R.json()
	CSRF_TOKEN = DATA['query']['tokens']['csrftoken']
	if not CSRF_TOKEN:
		sys.exit("Csrf Token acquisition failed!")

	completedSectionsFullPath = './CompletedSections.txt'
	if os.path.isfile(completedSectionsFullPath):
		outString = "Loading file: " + completedSectionsFullPath
		log(outString)
		print(outString)
		with open(completedSectionsFullPath, 'r') as file:
			completedPageSectionPairs = file.read().split('\n')
	else:
		completedPageSectionPairs = []
		with open(completedSectionsFullPath, 'w', newline='') as dataOut:
			dataOut.write('')

	# UPLOAD SECTION
	dirLoad = dirBase + '/VersionizedUploadData'
	dirAbLoad = dirLoad + '/' + Ab_String
	dirFvLoad = dirLoad + '/' + Fv_String
	dirQRLoad = dirLoad + '/' + QR_String
	dirQFLoad = dirLoad + '/' + QF_String
	dirRULoad = dirLoad + '/' + RU_String
	dirRPLoad = dirLoad + '/' + RP_String
	dirRKLoad = dirLoad + '/' + RK_String
	dirXPLoad = dirLoad + '/' + XP_String

	ItemDict = LoadJson(dirBase + '/Jsons', 'items.json', True)

	for f in os.listdir(dirLoad):
		if f.endswith('.txt'):
			if '#' in f:
				page, section = f[4:-4].replace('~', '/').replace('@', ':').split('#')
				if page + '#' + section not in completedPageSectionPairs:
					sectionNumber = getSectionNumber(page, section)
					if sectionNumber is not None and not sectionNumber == -1:
						sectionText = LoadTextFile(dirLoad, f)
						summary = 'Bot added info for game version v' + gameVersion + ', bot version ' + botVersion + '. Contact [[User:Alleryn]] for issues concerning this bot edit.'
						editSection(page, section, sectionNumber, sectionText, summary)
			else:
				page = f[4:-4].replace('~', '/').replace('@', ':')
				if page not in completedPageSectionPairs:
					text = LoadTextFile(dirLoad, f)
					summary = 'Bot added info for game version v' + gameVersion + ', bot version ' + botVersion + '. Contact [[User:Alleryn]] for issues concerning this bot edit.'
					editPage(page, text, summary)

	for f in os.listdir(dirXPLoad):
		if f.endswith('.txt'):
			page = 'Xptables/' + f[7:-4]
			if page not in completedPageSectionPairs:
				text = LoadTextFile(dirXPLoad, f)
				summary = 'Bot added info for game version v' + gameVersion + ', bot version ' + botVersion + '. Contact [[User:Alleryn]] for issues concerning this bot edit.'
				editPage(page, text, summary)

	for f in os.listdir(dirRKLoad):
		if f.endswith('.txt'):
			page = 'Category:Items/' + f[7:-4]
			section = 'Using_in_Recipes'
			if not page + '#' + section in completedPageSectionPairs:
				sectionNumber = getSectionNumber(page, section)
				sectionText = LoadTextFile(dirRKLoad, f)
				summary = 'Bot added info for game version v' + gameVersion + ', bot version ' + botVersion + '. Contact [[User:Alleryn]] for issues concerning this bot edit.'
				if sectionNumber == -1:
					PARAMS_EditPage = {"action": "edit", "format": 'json', "text": sectionText, "title": page, "summary": summary, "bot": '1', "token": CSRF_TOKEN}
					log('Editing ' + page + '#' + section)
					R = S.post(URL, data=PARAMS_EditPage)
					DATA = R.json()

					if "edit" in DATA and "result" in DATA["edit"] and "Success" == DATA["edit"]["result"]:
						with open(completedSectionsFullPath, 'a', newline='') as dataOut:
							dataOut.write(DATA["edit"]["title"] + '#' + section + '\n')
					else:
						outString = 'Failed ' + ' to edit ' + page + '#' + section
						print(outString)
						print(DATA)
						log(outString)
						log(DATA)
						sys.exit()
				elif sectionNumber is not None:
					editSection(page, section, sectionNumber, sectionText, summary)

	UploadSectionForEachItemPage(Ab_String, dirAbLoad)
	UploadSectionForEachItemPage(Fv_String, dirFvLoad)
	UploadSectionForEachItemPage(QR_String, dirQRLoad)
	UploadSectionForEachItemPage(QF_String, dirQFLoad)
	UploadSectionForEachItemPage(RU_String, dirRULoad)
	UploadSectionForEachItemPage(RP_String, dirRPLoad)
	# End UPLOAD SECTION

	PARAMS_DoLogout = {"action": "logout", "token": CSRF_TOKEN, "format": "json"}
	log('Logging out')
	R = S.post(URL, data=PARAMS_DoLogout)
	DATA = R.json()
	print(DATA)

	dirPython = dirBase + '/Python'
	MakeDir(dirPython)

	log('Archiving Python files')
	ArchivePyFiles('.')
	ArchivePyFiles('./Generators')
	os.rename(completedSectionsFullPath, dirBase + './CompletedSections.txt')

	log('Archiving Data')
	oldVersion = str(int(botVersion)-1)
	dirOld = './Data/' + oldVersion
	os.rename(dirOld, './Archive/Data/' + oldVersion)

	log('Updating botVersion.txt')
	with open('./BotVersion.txt', 'w', newline='') as dataOut:
		dataOut.write(str(int(botVersion)+1))


if __name__ == "__main__":
	main()