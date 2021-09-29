import os
import urllib.request

from Util import LoadJson, LoadTextFile, SaveJson, MakeDir, SaveTextFile

def getSkillText(skill_):
	if skill_ == "Unknown":
		skillText = "Unknown"
	elif skill_ in SkillJson:
		if "Name" in SkillJson[skill_]:
			skillText = '[[' + SkillJson[skill_]['Name'] + ']]'
		else:
			skillText = '[[' + skill_ + ']]'
	else:
		skillText = "Not found"
		print('ERROR. Skill ' + skill_ + ' not found in SkillDict.')
	return skillText

def getIconString(iconId):
	return '<span class="extimage32px">http://cdn.projectgorgon.com/' + '__GAMEVERSION__' + '/icons/icon_' + str(iconId) + '.png</span>'


os.chdir(os.path.dirname(os.path.abspath(__file__)))

gameVersion = urllib.request.urlopen('http://client.projectgorgon.com/fileversion.txt').read().decode('UTF-8')
dirJsons = './Jsons/v' + gameVersion

ItemJson = LoadJson(dirJsons, "items.json", True)
AbilityJson = LoadJson(dirJsons, "abilities.json", True)
SkillJson = LoadJson(dirJsons, "skills.json", True)
NpcJson = LoadJson(dirJsons, "npcs.json", True)
QuestJson = LoadJson(dirJsons, "quests.json", True)
RecipeJson = LoadJson(dirJsons, "recipes.json", True)
AttributeJson = LoadJson(dirJsons, "attributes.json", True)
LorebookJson = LoadJson(dirJsons, "lorebooks.json", True)
NpcLocJson = LoadJson(dirJsons, "npclocations.json", True)

# Add relevant information to Jsons

# Handle dupes
ItemJson["item_46517"]["Name"] = "Daisy (Lute)"

itemNameSet = set()
itemDupeSet = set()
for item in ItemJson:
	itemName = ItemJson[item]["Name"]
	if itemName in itemNameSet:
		itemDupeSet.add(itemName)
	else:
		itemNameSet.add(itemName)
goodDupes = {"item_15025", "item_6042", "item_6020", "item_6058", "item_5406", "item_6049", "item_6062", "item_6064", "item_6072"}  # Superjump Potion (non-event), the 8 foods that can be poisonsed
# "item_10305", "item_46517" Daisy (the flower), Daisy (the lute)
poisonedDupes = {"item_6401", "item_6402", "item_6403", "item_6404", "item_6405", "item_6406", "item_6407", "item_5409"}

for item in ItemJson:
	if ItemJson[item]["Name"] in itemDupeSet and item not in goodDupes:
		ItemJson[item]["BadDupe"] = True
	if "Keywords" in ItemJson[item] and "EquipSlot" in ItemJson[item] and "Lint_NotObtainable" in ItemJson[item]["Keywords"]:
		ItemJson[item]["UnobtainableEquipment"] = True
	if item in poisonedDupes:
		ItemJson[item]["Link"] = "Poisoned Food (no wiki page)"
	elif "BadDupe" in ItemJson[item] or "UnobtainableEquipment" in ItemJson[item]:
		ItemJson[item]["Link"] = "None"
	else:
		itemName = ItemJson[item]["Name"]
		itemPage = itemName
		if '#' in itemName:
			itemPage = itemPage.replace('#', "").replace(' ', '_')
		for lorebook in LorebookJson:
			if LorebookJson[lorebook]["Title"] == itemName:
				itemPage += '_(Item)'
				break
		ItemJson[item]["Page"] = itemPage
		if itemName == itemPage:
			ItemJson[item]["Link"] = '[[' + itemPage + ']]'
		else:
			ItemJson[item]["Link"] = '[[' + itemPage + '|' + itemName + ']]'
	if "IconId" in ItemJson[item]:
		ItemJson[item]["IconString"] = getIconString(ItemJson[item]["IconId"])
	else:
		ItemJson[item]["IconString"] = "None"
		print(ItemJson[item]["Name"] + ' has no IconId')

for ability in AbilityJson:
	AbilityJson[ability]["SkillText"] = getSkillText(AbilityJson[ability]["Skill"])
	if "IconID" in AbilityJson[ability]:
		AbilityJson[ability]["IconString"] = getIconString(AbilityJson[ability]["IconID"])
	else:
		AbilityJson[ability]["IconString"] = "None"
		print(AbilityJson[ability]["Name"] + ' has no IconID')
	abilityLink = '[[' + AbilityJson[ability]["Name"] + ']]'
	for skill in SkillJson:
		if getSkillText(skill) == abilityLink:
			AbilityJson[ability]["Link"] = '[[' + AbilityJson[ability]["Name"] + '_(ability)|' + AbilityJson[ability]["Name"] + ']]'
	for item in ItemJson:
		if ItemJson[item]["Link"] == abilityLink:
			AbilityJson[ability]["Link"] = '[[' + AbilityJson[ability]["Name"] + '_(ability)|' + AbilityJson[ability]["Name"] + ']]'
	if "Link" not in AbilityJson[ability]:
		AbilityJson[ability]["Link"] = abilityLink

NpcJson["NPC_Cinnamon"]["Link"] = "[[Cinnamon the rabbit]]"
NpcJson["NPC_Sugar"]["Link"] = "[[Sugar (NPC)]]"
NpcJson["NPC_Daisy"]["Link"] = "[[Daisy (NPC)]]"
for npc in NpcJson:
	if npc in ["NPC_Velkort_Halloween", "AdminTestNpc", "NPC_Placeholder", "NPC_AuShin", "NPC_Vughal", "WerewolfAltar", "NPC_Gonchakal", "NPC_SpiderPlaceholder", "TapestryInnChest", "NPC_AkhisasRepresentative", "KhyrulekMementoChest", "IvynsChest", "WardenStorageChest", "GuildAltar", "RigersChest", "KurMountainsWorkOrderSign", "DalvosChest", "TutorialChest", "WinterCourtEntranceChest", "FaeRealm1WorkOrderSign", "Desert1WorkOrderSign", "CasinoWorkOrderSign", "RahuWorkOrderSign", "SunValeWorkOrderSign", "EltibuleWorkOrderSign", "SerbuleWorkOrderSign"]:
		NpcJson[npc]["Blacklisted"] = True
	if npc in NpcLocJson:
		NpcJson[npc]["Location"] = NpcLocJson[npc]["Location"]
	if "Link" not in NpcJson[npc]:
		if "Blacklisted" in NpcJson[npc]:
			NpcJson[npc]["Link"] = "None"
		else:
			NpcJson[npc]["Link"] = '[[' + NpcJson[npc]["Name"] + ']]'

QuestJson["quest_1"]["Blacklisted"] = True  # "Kill Skeletons"
QuestJson["quest_2"]["Blacklisted"] = True  # "Find Gravestones"
QuestJson["quest_10004"]["Link"] = "[[Old Fangsworth (Quest)]]"
QuestJson["quest_15004"]["Link"] = "[[The Mauler (Quest)]]"
for quest in QuestJson:
	if "Link" not in QuestJson[quest]:
		if "Blacklisted" in QuestJson[quest]:
			QuestJson[quest]["Link"] = None
		elif "Keywords" in QuestJson[quest] and "WorkOrder" in QuestJson[quest]['Keywords']:
			QuestJson[quest]["Link"] = None
			QuestJson[quest]["WorkOrder"] = True
		else:
			questName = QuestJson[quest]["Name"]
			questLink = '[[' + questName + ']]'
			for item in ItemJson:
				if ItemJson[item]["Link"] == questLink:
					ItemJson[item]["SharedQuest"] = True
					QuestJson[quest]["SharedItem"] = True
					QuestJson[quest]["Link"] = '[[' + questName + '_(Quest)]]'
			if "Link" not in QuestJson[quest]:
				QuestJson[quest]["Link"] = questLink

RecipeJson["recipe_5215"]["Description"] = "Receive +6 Indirect Cold Mitigation, plus the two combos from a Meditation Pillar."  # Orcish Meditation #15 has unusual syntax, moving the +6 in front of Indirect Cold Mitigation
RecipeJson["recipe_6046"]["Description"] = "Gain access to a combo that affects all enemies within 5 meters and reduces their Rage by 30. Also gain a passive insight: all attacks generate 7% less Rage in your targets."  # Calligraphy: Lethargic+ is missing a period.
RecipeJson["recipe_6505"]["Description"] = "Gain insight: +5% Crushing Attack Damage. (Stacks with regular calligraphy effects)"  # Secret Calligraphy: Fist is missing a period.

for recipe in RecipeJson:
	resultCode = 0
	ingredientConsumeUses = ''
	numberConsumeUses = 0
	expectResults = True
	consumeItemUsesCheck = False
	recipeTypes = set()
	if "ResultEffects" in RecipeJson[recipe]:
		for resultEffect in RecipeJson[recipe]["ResultEffects"]:
			if resultEffect.startswith('Decompose'):
				expectResults = False
				recipeTypes.add('Decompose')
			elif resultEffect.startswith('Research'):
				expectResults = False
				recipeTypes.add('Research')
			elif resultEffect.startswith('SpawnPremonition'):
				expectResults = False
				recipeTypes.add('SpawnPremonition')
			elif resultEffect.startswith('Meditation'):
				expectResults = False
				recipeTypes.add('Meditation')
			elif resultEffect.startswith('Calligraphy'):
				expectResults = False
				recipeTypes.add('Calligraphy')
			elif resultEffect.startswith('CraftingEnhanceItem'):
				expectResults = False
				recipeTypes.add('CraftingEnhanceItem')
				craftingEnhanceData = resultEffect.replace('CraftingEnhanceItem', '').replace(')', '').partition('(')
				craftingEnhanceType = craftingEnhanceData[0]
				craftingEnhanceValues = craftingEnhanceData[2].partition(',')
				craftingEnhanceMagnitude = craftingEnhanceValues[0]
				craftingEnhancePoints = craftingEnhanceValues[2]
				if craftingEnhanceType.endswith('Mod'):
					RecipeJson[recipe]["ResultString"] = "Adds '''+" + str(int(100 * float(craftingEnhanceMagnitude))) + '% Direct ' + craftingEnhanceType.replace('Mod', '') + " Damage'''.<br>Consumes '''" + craftingEnhancePoints + " Enhancement Points'''."
				else:
					RecipeJson[recipe]["ResultString"] = "Adds '''+" + craftingEnhanceMagnitude + ' ' + craftingEnhanceType + "'''.<br>Consumes '''" + craftingEnhancePoints + " Enhancement Points'''."
			elif resultEffect.startswith('AddItemTSysPower'):
				expectResults = False
				if resultEffect.startswith('AddItemTSysPowerWax'):
					recipeTypes.add('AddItemTSysPowerWax')
				else:
					recipeTypes.add('AddItemTSysPower')
			# elif resultEffect.startswith('CreateMiningSurvey'):
			# 	expectResults = False
			# 	recipeTypes.add('CreateMiningSurvey')
			# 	resultInternal = resultEffect.replace(')', '').partition('(')[2]
			# 	for item in ItemJson:
			# 		if ItemJson[item]["InternalName"] == resultInternal:
			# 			resultCode = int(item[5:])
			# 			break
			# elif resultEffect.startswith('CreateGeologySurvey'):
			# 	expectResults = False
			# 	recipeTypes.add('CreateGeologySurvey')
			# 	resultInternal = resultEffect.replace(')', '').partition('(')[2]
			# 	for item in ItemJson:
			# 		if ItemJson[item]["InternalName"] == resultInternal:
			# 			resultCode = int(item[5:])
			# 			break
			elif resultEffect.startswith('Create'):  # Treasure Map plus Geology/Mineral Surveys
				expectResults = False
				recipeTypes.add('Create')
				resultInternal = RecipeJson[recipe]["InternalName"]
				for item in ItemJson:
					if ItemJson[item]["InternalName"] == resultInternal:
						resultCode = int(item[5:])
						break
			elif resultEffect.startswith('ExtractTSysPower'):
				expectResults = False
				recipeTypes.add('ExtractTSysPower')
				resultInternal = resultEffect.replace('ExtractTSysPower(', '').partition(',')[0]
				for item in ItemJson:
					if ItemJson[item]["InternalName"] == resultInternal:
						resultCode = int(item[5:])
						break
			elif resultEffect.startswith('TSysCraftedEquipment') or resultEffect.startswith('GiveTSysItem') or resultEffect.startswith('Whittling'):
				expectResults = False
				if "ProtoResultItems" not in RecipeJson[recipe]:
					print(RecipeJson[recipe]["Name"] + ' has TSysCraftedEquipment or GiveTSysItem or Whittling but no ProtoResultItems.')
				else:
					recipeTypes.add('ProtoResultItems')
			elif resultEffect.startswith('ConsumeItemUses'):
				consumeItemUsesCheck = True
				consumeUsesData = resultEffect.replace('ConsumeItemUses(', '').replace(')', '').partition(',')
				ingredientConsumeUses = consumeUsesData[0]
				numberConsumeUses = consumeUsesData[2]
	if not RecipeJson[recipe]["ResultItems"]:
		if expectResults:
			print(RecipeJson[recipe]["Name"] + ' expected ResultItems.')
	else:
		if not expectResults:
			print(RecipeJson[recipe]["Name"] + ' expected no ResultItems.')
		else:
			recipeTypes.add('ResultItems')
	if len(recipeTypes) > 1:
		print(RecipeJson[recipe]["Name"] + ' has multiple types.')
	elif len(recipeTypes) == 0:
		if "ResultEffects" in RecipeJson[recipe]:
			print(RecipeJson[recipe]["Name"] + ' has no type. ResultEffects are: ' + str(RecipeJson[recipe]["ResultEffects"]))
		else:
			print(RecipeJson[recipe]["Name"] + ' has no type and no ResultEffects.')
	else:  # recipeTypes has length 1
		if recipeTypes == {'SpawnPremonition'}:
			RecipeJson[recipe]["ResultString"] = RecipeJson[recipe]["Description"].replace('\n\n', '<br>')  # These descriptions have a double newline.  Could just leave it, but a <br> is probably tidier.
		elif recipeTypes == {'Meditation'}:
			desc = RecipeJson[recipe]["Description"].rstrip()  # For some reason a lot fo the meditation descriptions end with a \n newline
			if desc.startswith('Receive the '):
				RecipeJson[recipe]["ResultString"] = desc
			elif desc.startswith('Receive +'):
				descParts = desc.replace('Receive ', '', 1).partition(',')
				if descParts[1] == ',':
					RecipeJson[recipe]["ResultString"] = "Receive '''" + descParts[0] + "'''," + descParts[2]
				else:
					print('Meditation recipe ' + RecipeJson[recipe]["Name"] + ' has no comma after plus sign.')
			else:
				print('Meditation recipe ' + RecipeJson[recipe]["Name"] + ' has an unusual start to the string.')
		elif recipeTypes == {'Calligraphy'}:
			desc = RecipeJson[recipe]["Description"]
			descParts1 = desc.partition('insight: ')
			if descParts1[1] == 'insight: ':
				descParts2 = descParts1[2].partition('.')
				if descParts2[1] == '.':
					RecipeJson[recipe]["ResultString"] = descParts1[0] + "insight: '''" + descParts2[0] + "'''." + descParts2[2]
				else:
					print('Calligraphy recipe ' + RecipeJson[recipe]["Name"] + ' has no period after "insight: ".')
			else:
				RecipeJson[recipe]["ResultString"] = desc
		# elif recipeTypes == {'CraftingEnhanceItem'}:
		elif recipeTypes == {'AddItemTSysPower'}:
			desc = RecipeJson[recipe]["Description"]
			descParts1 = desc.partition('with the following power: ')
			if descParts1[1] == 'with the following power: ':
				descParts2 = descParts1[2].partition('. Uses 100')
				if descParts2[1] == '. Uses 100':
					RecipeJson[recipe]["ResultString"] = descParts1[0] + "with the following power: '''" + descParts2[0] + "'''.<br>Uses 100" + descParts2[2]
				else:
					print('Shamanic Infusion recipe ' + RecipeJson[recipe]["Name"] + ' has no ". Uses 100" after "with the following power: ".')
			else:
				print('Shamanic Infusion recipe ' + RecipeJson[recipe]["Name"] + ' not parsing as expected.')
		elif recipeTypes == {'AddItemTSysPowerWax'}:
			desc = RecipeJson[recipe]["Description"]
			descParts1 = desc.partition('with the following power: ')
			if descParts1[1] == 'with the following power: ':
				descParts2 = descParts1[2].partition('. The wax lasts')
				if descParts2[1] == '. The wax lasts':
					RecipeJson[recipe]["ResultString"] = descParts1[0] + "with the following power: '''" + descParts2[0] + "'''.<br>The wax lasts" + descParts2[2]
				else:
					print('Shield wax recipe ' + RecipeJson[recipe]["Name"] + ' has no ". The wax lasts" after "with the following power: ".')
			else:
				print('Shield wax recipe ' + RecipeJson[recipe]["Name"] + ' not parsing as expected.')
		elif recipeTypes == {'Create'} or recipeTypes == {'ExtractTSysPower'}:
			RecipeJson[recipe]["ResultItems"] = [{"ItemCode": resultCode, "StackSize": 1}]
		elif recipeTypes == {'ProtoResultItems'}:
			RecipeJson[recipe]["ResultItems"] = RecipeJson[recipe]["ProtoResultItems"]
		elif recipeTypes == {'ResultItems'} and consumeItemUsesCheck:
			for ingredient in RecipeJson[recipe]["Ingredients"]:
				if "ItemKeys" in ingredient and ingredientConsumeUses in ingredient["ItemKeys"]:
					ingredient["ConsumeUses"] = int(numberConsumeUses)

	RecipeJson[recipe]["SkillText"] = getSkillText(RecipeJson[recipe]["Skill"])
	for ingredient in RecipeJson[recipe]['Ingredients']:
		if "ItemCode" in ingredient:
			ingredient["Link"] = ItemJson['item_' + str(ingredient["ItemCode"])]["Link"]
			ingredient["IconString"] = ItemJson['item_' + str(ingredient["ItemCode"])]["IconString"]
	for result in RecipeJson[recipe]['ResultItems']:
		if "ItemCode" in result:
			result["Link"] = ItemJson['item_' + str(result["ItemCode"])]["Link"]
			result["IconString"] = ItemJson['item_' + str(result["ItemCode"])]["IconString"]

botVersion = LoadTextFile('.', 'BotVersion.txt')

dirData = './Data'
MakeDir(dirData)
dirVersion = dirData + '/' + botVersion
MakeDir(dirVersion)
dirSave = dirVersion + '/Jsons'
MakeDir(dirSave)

SaveTextFile(dirVersion, botVersion + '_GameVersion.txt', gameVersion)
SaveJson(dirSave, 'items.json', ItemJson)
SaveJson(dirSave, 'abilities.json', AbilityJson)
SaveJson(dirSave, 'skills.json', SkillJson)
SaveJson(dirSave, 'npcs.json', NpcJson)
SaveJson(dirSave, 'quests.json', QuestJson)
SaveJson(dirSave, 'recipes.json', RecipeJson)
SaveJson(dirSave, 'attributes.json', AttributeJson)
