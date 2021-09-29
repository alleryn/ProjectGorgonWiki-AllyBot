from .GeneratorGlobalStrings import versionString, botInfoString
from .WikiGetItemCategoryLink import getItemCategoryLink

def GenerateWikiItemQuestData(target, targetDict, QuestDict, NpcDict):
	# * GET TARGET ITEM DATA *
	print("Getting quest data for " + target)
	targetInternalName = targetDict['InternalName']
	print('target internal name = ' + targetInternalName)
	targetKeywordList = []
	if "Keywords" in targetDict:
		targetKeywordList = [itemKeyword.split("=", 1)[0] for itemKeyword in targetDict['Keywords']]
		print('target keyword list = ' + str(targetKeywordList))

	# * GET QUEST DATA *
	def GetQuestInfo(gqiQuest):
		questLink = QuestDict[gqiQuest]['Link']
		notes = []
		questNpc = 'Unknown'
		location = 'Unknown'
		cooldown = 'One time only'
		minFavor = 'Unknown'
		if "FavorNpc" in QuestDict[gqiQuest]:
			favorNpc = QuestDict[gqiQuest]['FavorNpc'].split("/", 1)[-1]
			if favorNpc in NpcDict:
				questNpc = NpcDict[favorNpc]["Link"]
				location = NpcDict[favorNpc]["Location"]
		if location == 'Unknown' and "DisplayedLocation" in QuestDict[gqiQuest]:
			location = QuestDict[gqiQuest]['DisplayedLocation']
		for key in QuestDict[gqiQuest]:
			if key.startswith('ReuseTime_'):
				timeUnits = key[10:]
				numUnits = QuestDict[gqiQuest][key]
				cooldown = str(numUnits) + ' ' + timeUnits
		if "Requirements" in QuestDict[gqiQuest] and type(QuestDict[gqiQuest]['Requirements']) is list:
			for questRequirement in QuestDict[gqiQuest]['Requirements']:
				if ("Skill" in questRequirement and questRequirement['Skill'] == "Race_Fae") or ("AllowedRace" in questRequirement and questRequirement['AllowedRace'] == "Fae"):
					notes.append('Fairy-only')
				if "T" in questRequirement:
					if "IsWarden" == questRequirement["T"]:
						notes.append('Warden-only')
					if "IsLongtimeAnimal" == questRequirement["T"]:
						notes.append('Long time animal only')
					if "MinFavorLevel" == questRequirement["T"] and "Level" in questRequirement:
						minFavor = questRequirement["Level"]
		return questLink, questNpc, minFavor, location, cooldown, notes

	questsWithRewardItem = []
	questsWithObjectiveItem = []
	workOrderData = ''
	for quest in QuestDict:
		if "Rewards_Items" in QuestDict[quest]:
			for rewardItem in QuestDict[quest]['Rewards_Items']:
				if "Item" in rewardItem:
					if rewardItem['Item'] == targetInternalName:
						stackSize = rewardItem['StackSize']
						questInfo = GetQuestInfo(quest)
						questsWithRewardItem.append('|-\n| ' + questInfo[0] + ' || style="text-align:center;" | ' + str(stackSize) + ' || ' + questInfo[4] + ' || ' + questInfo[1] + ' || ' + questInfo[2] + ' || ' + questInfo[3] + ' || ' + ','.join(questInfo[5]) + '\n')
		if "Objectives" in QuestDict[quest]:
			objectiveList = []
			keywordObjectiveList = []
			for objective in QuestDict[quest]['Objectives']:
				if "ItemName" in objective:
					if objective['ItemName'] == targetInternalName:
						if "Keywords" in QuestDict[quest] and "WorkOrder" in QuestDict[quest]['Keywords']:  # (non-keyword work order)
							if "Number" in objective:
								number = objective["Number"]
							else:
								number = 0
								print('Work Order ' + QuestDict[quest]["Name"] + ' has objective with no number.')
							councils = 0
							if "Rewards" in QuestDict[quest]:
								for reward in QuestDict[quest]['Rewards']:
									if "Amount" in reward and "Currency" in reward and reward['Currency'] == "Gold":
										councils = reward['Amount']
							else:
								print('Work Order ' + QuestDict[quest]["Name"] + ' has ill defined gold rewards field')
							level = 0
							if "Requirements" in QuestDict[quest]:
								for requirement in QuestDict[quest]['Requirements']:
									flag = True
									if "Skill" in requirement and requirement['Skill'] == "Industry" and "Level" in requirement:
										level = requirement['Level']
										flag = False
									if flag:
										print('Work Order ' + QuestDict[quest]["Name"] + ' has strange Requirements field (either /Skill is not Industry or /Level is not present)')
							targetNpc = ""
							for objective2 in QuestDict[quest]['Objectives']:
								if "Description" in objective2 and objective2['Description'].startswith("Deliver to "):
									targetNpc = objective2['Description'].replace("Deliver to ", "")
							if not targetNpc:
								targetNpc = "Not found"
								print('Work Order ' + QuestDict[quest]["Name"] + ' found no targetNpc')
							workOrderData += 'Turn in ' + str(number) + 'x ' + targetDict["Link"] + ' to [[' + targetNpc + ']] for ' + str(councils) + ' councils. Requires [[Industry]] Level ' + str(level) + '.'
							if QuestDict[quest]['Name'].endswith("(Seasonal)"):
								workOrderData += ' Available only seasonally.'
							workOrderData += '\n'
						else:  # "Standard" (non-keyword non- work order)
							if "Type" in objective:
								if objective["Type"] == "GuildGiveItem":
									objectiveType = "Amass with Guild"
								else:
									objectiveType = objective["Type"]
							else:
								objectiveType = "Not Found"
								print('Quest ' + QuestDict[quest]["Name"] + ' has objective with no type.')
							if "Number" in objective:
								number = str(objective["Number"])
							else:
								number = "Not found"
								print('Quest ' + QuestDict[quest]["Name"] + ' has objective with no number.')
							objectiveList.append((objectiveType, number))
				# end if "ItemName" in objective:
				if "ItemKeyword" in objective and "Type" in objective and objective['Type'] == "GuildGiveItem":
					if objective['ItemKeyword'] in targetKeywordList:
						itemCategory = objective['ItemKeyword']
						objectiveType = "Amass with Guild"
						if "Number" in objective:
							number = str(objective["Number"])
						else:
							number = "Not found"
							print('Quest ' + QuestDict[quest]["Name"] + ' has keyword-style objective with no number.')
						keywordObjectiveList.append((objectiveType, number, itemCategory))
				elif "Target" in objective and "Type" in objective:  # In this case Target might be an item category name (keyword) or might not, it can also be an npc for example
					if objective['Target'] in targetKeywordList and (objective['Type'] == "Collect" or objective['Type'] == "Have" or objective['Type'] == "Harvest"):
						if "Keywords" in QuestDict[quest] and "WorkOrder" in QuestDict[quest]['Keywords']:  # (keyword work order)
							if "Number" in objective:
								number = objective["Number"]
							else:
								number = 0
								print('Work Order ' + QuestDict[quest]["Name"] + ' has objective with no number.')
							councils = 0
							if "Rewards" in QuestDict[quest]:
								for reward in QuestDict[quest]['Rewards']:
									if "Amount" in reward and "Currency" in reward and reward['Currency'] == "Gold":
										councils = reward['Amount']
							else:
								print('Work Order ' + QuestDict[quest]["Name"] + ' has ill defined gold rewards field')
							level = 0
							if "Requirements" in QuestDict[quest]:
								for requirement in QuestDict[quest]['Requirements']:
									flag = True
									if "Skill" in requirement and requirement['Skill'] == "Industry" and "Level" in requirement:
										level = requirement['Level']
										flag = False
									if flag:
										print('Work Order ' + QuestDict[quest]["Name"] + ' has strange Requirements field (either /Skill is not Industry or /Level is not present)')
							targetNpc = ""
							for objective2 in QuestDict[quest]['Objectives']:
								if "Description" in objective2 and objective2['Description'].startswith("Deliver to "):
									targetNpc = objective2['Description'].replace("Deliver to ", "")
							if not targetNpc:
								targetNpc = "Not found"
								print('Work Order ' + QuestDict[quest]["Name"] + ' found no targetNpc')
							workOrderData += 'Turn in any ' + str(number) + 'x ' + getItemCategoryLink(objective['Target']) + ' to [[' + targetNpc + ']] for ' + str(councils) + ' councils. Requires [[Industry]] Level ' + str(level) + '.'
							if QuestDict[quest]['Name'].endswith("(Seasonal)"):
								workOrderData += ' Available only seasonally.'
							workOrderData += '\n'
						else:  # (keyword non-work order)
							itemCategory = objective['Target']
							objectiveType = objective['Type']
							if "Number" in objective:
								number = str(objective["Number"])
							else:
								number = "Not found"
								print('Quest ' + QuestDict[quest]["Name"] + ' has keyword-style objective with no number.')
							keywordObjectiveList.append((objectiveType, number, itemCategory))
			# end for objective in QuestDict[quest]['Objectives']:
			if objectiveList or keywordObjectiveList:  # objectiveList should only be pythonically 'true' (i.e. non-empty) in the non-work order case. (An alternative ordering of the nested ifs is possible
				# in order to make this more clear, but this also has some drawbacks, in that "Keywords" (used to check for work order) will exist more
				# often than objective["Item Name"] will = targetInternalName, so i suspect the alternate nesting would be slower).
				objectiveTypes = set(x[0] for x in objectiveList) | set(y[0] for y in keywordObjectiveList)  # Set union
				if not objectiveTypes == {"Harvest"}:  # Eliminate quests whose only objective is harvest, since simple possession of the item isn't useful in this case.  I.e. it isn't a "Use" of the item itself.
					questInfo = GetQuestInfo(quest)
					objectivesData = '<br>'.join([objective[1] + ' (' + objective[0] + ')' for objective in objectiveList])
					keywordObjectivesData = '<br>'.join([keywordObjective[1] + ' (' + keywordObjective[0] + ' any ' + getItemCategoryLink(keywordObjective[2]) + ')' for keywordObjective in keywordObjectiveList])
					if objectivesData and keywordObjectivesData:
						objString = "Error"
						print('Error. Quest + ' + QuestDict[quest]["Name"] + ' has both objectives and keyword objectives.')
					else:
						objString = objectivesData + keywordObjectivesData
					questsWithObjectiveItem.append('|-\n| ' + questInfo[0] + ' || ' + objString + ' || ' + questInfo[4] + ' || ' + questInfo[1] + ' || ' + questInfo[2] + ' || ' + questInfo[3] + ' || ' + ','.join(questInfo[5]) + '\n')
	# end for quest in QuestDict:

	# * STRINGIFY QUEST DATA *
	questsWithRewardSource = '===Quest Rewards===\n' + versionString + botInfoString
	if questsWithRewardItem:
		questsWithRewardSource += '{| {{STDT|sortable mw-collapsible mw-collapsed}}\n! Quest !! Number Acquired !! Quest Cooldown<br>(if repeatable) !! NPC !! Minimum Favor !! Location !! Notes\n'
		questsWithRewardSource += ''.join(questsWithRewardItem)
		questsWithRewardSource += '|}\n'
	else:
		questsWithRewardSource += 'None.\n'
	questsWithObjectiveSource = '===Quest Fulfillment===\n' + versionString + botInfoString
	if questsWithObjectiveItem or workOrderData:
		if questsWithObjectiveItem:
			questsWithObjectiveSource += '{| {{STDT|sortable mw-collapsible mw-collapsed}}\n! Quest !! Number Required !! Quest Cooldown<br>(if repeatable) !! NPC !! Minimum Favor !! Location !! Notes\n'
			questsWithObjectiveSource += ''.join(questsWithObjectiveItem)
			questsWithObjectiveSource += '|}\n'
		if workOrderData:
			questsWithObjectiveSource += '=====Work Order=====\n' + workOrderData
	else:
		questsWithObjectiveSource += 'None.\n'
	return questsWithRewardSource, questsWithObjectiveSource