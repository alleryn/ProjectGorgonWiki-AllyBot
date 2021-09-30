import os
import urllib.request
import sys

from Util import LoadTextFile, LoadJson, SaveTextFile, MakeDir
from Generators.WikiHardcoreDeathPenaltyItems import GenerateWikiHardcoreDeathPenaltyItems
from Generators.WikiFood import GenerateWikiFood
from Generators.WikiAttributes import GenerateWikiAttributes
from Generators.WikiItemAbilityData import GenerateWikiItemAbilityData
from Generators.WikiItemFavorData import GenerateWikiItemFavorData
from Generators.WikiItemQuestData import GenerateWikiItemQuestData
from Generators.WikiItemRecipeData import GenerateWikiItemRecipeData, GenerateWikiKeywordRecipeData
from Generators.WikiXpTableData import GenerateWikiXpTableData
from GlobalStrings import Ab_String, Fv_String, QR_String, QF_String, RU_String, RP_String, RK_String, XP_String

os.chdir(os.path.dirname(os.path.abspath(__file__)))

gameVersion = urllib.request.urlopen('http://client.projectgorgon.com/fileversion.txt').read().decode('UTF-8')
botVersion = LoadTextFile('.', 'BotVersion.txt')
dirBase = './Data/' + botVersion

if not gameVersion == LoadTextFile(dirBase, botVersion + '_GameVersion.txt'):
	sys.exit('**ERROR** GAME VERSION MISMATCH')

dirLoad = dirBase + '/Jsons'
dirSave = dirBase + '/WikiData'
MakeDir(dirSave)

ItemDict = LoadJson(dirLoad, "items.json", True)
AbilityDict = LoadJson(dirLoad, "abilities.json", True)
SkillDict = LoadJson(dirLoad, "skills.json", True)
NpcDict = LoadJson(dirLoad, "npcs.json", True)
QuestDict = LoadJson(dirLoad, "quests.json", True)
RecipeDict = LoadJson(dirLoad, "recipes.json", True)
AttributeDict = LoadJson(dirLoad, "attributes.json", True)
XpTableDict = LoadJson(dirLoad, "xptables.json", True)

# Use ~ for slash in filenames and @ for :
SaveTextFile(dirSave, botVersion + '_Hardcore_Mode#List_of_Items_Usable_Only_in_Hardcore_Mode.txt', GenerateWikiHardcoreDeathPenaltyItems(ItemDict))
ediblesSource, mealsSource, snacksSource, instantsSource = GenerateWikiFood(ItemDict, RecipeDict)
SaveTextFile(dirSave, botVersion + '_Gourmand~Edibles#Edibles.txt', ediblesSource)
SaveTextFile(dirSave, botVersion + '_Gourmand~Meals#Meals.txt', mealsSource)
SaveTextFile(dirSave, botVersion + '_Gourmand~Snacks#Snacks.txt', snacksSource)
SaveTextFile(dirSave, botVersion + '_Gourmand~Instant-Snacks#Instant-Snacks.txt', instantsSource)
attributeLabelsSource, attributeIconsSource = GenerateWikiAttributes(AttributeDict)
SaveTextFile(dirSave, botVersion + '_Template@Attribute_label.txt', attributeLabelsSource)
SaveTextFile(dirSave, botVersion + '_Template@Attribute_icon.txt', attributeIconsSource)


blacklistedItems = []
for item in ItemDict:
	if "BadDupe" in ItemDict[item] or "UnobtainableEquipment" in ItemDict[item]:
		blacklistedItems.append(item)
for item in blacklistedItems:
	del ItemDict[item]

blacklistedQuests = []
for quest in QuestDict:
	if "Blacklisted" in QuestDict[quest]:
		blacklistedQuests.append(quest)
for quest in blacklistedQuests:
	del QuestDict[quest]

blacklistedNpcs = []
for npc in NpcDict:
	if "Blacklisted" in NpcDict[npc]:
		blacklistedNpcs.append(npc)
for npc in blacklistedNpcs:
	del NpcDict[npc]

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

recipeKeywordSkips = {"Crystal", "CheapMeat", "Equipment", "MainHand", "OffHand", "Head", "Chest", "Legs", "Hands", "Feet", "Necklace", "Ring", "Shield"}

for keyword in recipeKeywordSkips :
	recipesSource = GenerateWikiKeywordRecipeData(keyword, RecipeDict)
	SaveTextFile(dirRKSave, botVersion + '_RK_' + keyword + '.txt', recipesSource)

for item in ItemDict:
	questRewardsSource, questFulfillmentSource = GenerateWikiItemQuestData(item, ItemDict[item], QuestDict, NpcDict)
	usingInRecipesSource, producingWithRecipesSource = GenerateWikiItemRecipeData(item, ItemDict[item], RecipeDict, recipeKeywordSkips)
	SaveTextFile(dirAbSave, botVersion + '_Ab_' + item + '.txt', GenerateWikiItemAbilityData(item, ItemDict[item], AbilityDict))
	SaveTextFile(dirFvSave, botVersion + '_Fv_' + item + '.txt', GenerateWikiItemFavorData(item, ItemDict[item], NpcDict))
	SaveTextFile(dirQRSave, botVersion + '_QR_' + item + '.txt', questRewardsSource)
	SaveTextFile(dirQFSave, botVersion + '_QF_' + item + '.txt', questFulfillmentSource)
	SaveTextFile(dirRUSave, botVersion + '_RU_' + item + '.txt', usingInRecipesSource)
	SaveTextFile(dirRPSave, botVersion + '_RP_' + item + '.txt', producingWithRecipesSource)

for xpTable in XpTableDict:
	xpTableSource = GenerateWikiXpTableData(XpTableDict[xpTable])
	SaveTextFile(dirXPSave, botVersion + '_XP_' + XpTableDict[xpTable]["InternalName"] + '.txt', xpTableSource)