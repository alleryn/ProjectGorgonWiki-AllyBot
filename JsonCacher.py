import os
import urllib.request

from Util import MakeDir, LoadJson, SaveJson, SaveTextFile
from Generators.WikiRecipeTemplate import GenerateWikiRecipeTemplate

os.chdir(os.path.dirname(os.path.abspath(__file__)))

version = urllib.request.urlopen('http://client.projectgorgon.com/fileversion.txt').read().decode('UTF-8')
print("version = " + version)

prefix = 'http://cdn.projectgorgon.com/v'
midfix = '/data/'
postfix = '.json'

dirJsons = './Jsons'
MakeDir(dirJsons)

dirSave = dirJsons + '/v' + version
MakeDir(dirSave)

JsonNames = [
	"abilities",
	"advancementtables",
	"ai",
	"areas",
	"attributes",
	"directedgoals",
	"effects",
	"items",
	"itemuses",
	"lorebookinfo",
	"lorebooks",
	"npcs",
	"playertitles",
	"quests",
	"recipes",
	"skills",
	"sources_abilities",
	"sources_items",
	"sources_recipes",
	"storagevaults",
	"tsysclientinfo",
	"xptables",
]

for name in JsonNames:
	fileName = dirSave + '/' + name + postfix

	if os.path.isfile(fileName):
		print("File ", fileName, " already exists")
	else:
		url = prefix + version + midfix + name + postfix
		print("Reading " + name + ".json from " + url)
		dataIn = urllib.request.urlopen(url).read().decode('UTF-8')

		print("Caching " + name + " json")
		with open(fileName, 'w', newline='') as dataOut:
			dataOut.write(dataIn)

ItemDict = LoadJson(dirSave, 'items.json', False)

keywordSet = set()
for item in ItemDict:
	if "Keywords" in ItemDict[item]:
		for keyword in ItemDict[item]['Keywords']:
			keyword = keyword.split("=", 1)[0]
			keywordSet.add(keyword)
SaveJson(dirSave, 'itemKeywords.json', sorted(keywordSet))

keywordSetPrevious = set(LoadJson(dirJsons + '/v' + str(int(version) - 1), 'itemKeywords.json', False))

removedKeywords = sorted(keywordSetPrevious - keywordSet)
SaveTextFile(dirSave, 'removedKeywords.txt', str(removedKeywords))

addedKeywords = sorted(keywordSet - keywordSetPrevious)
SaveTextFile(dirSave, 'addedKeywordsForWiki.txt', '\n'.join('|' + kw + ' = ' for kw in addedKeywords))
SaveTextFile(dirSave, 'addedKeywordsForPython.txt', '\n'.join('elif keyword == "' + kw + '":\n\tplural = ""' for kw in addedKeywords))

NpcDict = LoadJson(dirSave, 'npcs.json', False)
npcList = sorted(NpcDict.keys())
SaveJson(dirSave, 'npcList.json', npcList)

npcListPrevious = LoadJson(dirJsons + '/v' + str(int(version) - 1), 'npcList.json', False)

removedNpcs = sorted(set(npcListPrevious) - set(npcList))
SaveTextFile(dirSave, 'removedNpcs.txt', str(removedNpcs))

addedNpcs = sorted(set(npcList) - set(npcListPrevious))
SaveTextFile(dirSave, 'addedNpcsForNpclocationsJson.txt', ''.join(',\n"' + npc + '": {\n\t"Location": "",\n\t"Name": "' + NpcDict[npc]["Name"] + '"\n}' for npc in addedNpcs))

RecipeDict = LoadJson(dirSave, 'recipes.json', False)
recipeList = sorted(RecipeDict.keys())
SaveJson(dirSave, 'recipeList.json', recipeList)

recipeListPrevious = LoadJson(dirJsons + '/v' + str(int(version) - 1), 'recipeList.json', False)

removedRecipes = sorted(set(recipeListPrevious) - set(recipeList))
SaveTextFile(dirSave, 'removedRecipes.txt', str(removedRecipes))

RecipeSourcesDict = LoadJson(dirSave, 'sources_recipes.json', False)
addedRecipes = set(recipeList) - set(recipeListPrevious)
SaveTextFile(dirSave, 'addedRecipesForRecipeTemplate.txt', GenerateWikiRecipeTemplate(addedRecipes, RecipeDict, ItemDict, RecipeSourcesDict))

removedItems = set()
nameChangedItems = set()
ItemDictPrev = LoadJson(dirJsons + '/v' + str(int(version) - 1), 'items.json', False)
for item in ItemDictPrev:
	if item not in ItemDict:
		removedItems.add(ItemDictPrev[item]["Name"] + ": " + item)
	elif ItemDict[item]["Name"] != ItemDictPrev[item]["Name"]:
		nameChangedItems.add(ItemDictPrev[item]["Name"] + ": " + item + " is now " + ItemDict[item]["Name"])
SaveTextFile(dirSave, 'removedItems.txt', '\n'.join(sorted(removedItems)))
SaveTextFile(dirSave, 'nameChangedItems.txt', '\n'.join(sorted(nameChangedItems)))

oldVersion = str(int(version)-1)
dirOld = dirJsons + '/v' + oldVersion
os.rename(dirOld, 'Archive' + dirOld)