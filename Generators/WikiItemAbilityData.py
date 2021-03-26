from .GeneratorGlobalStrings import versionString, botInfoString

def GenerateWikiItemAbilityData(target, targetDict, AbilityDict):
	# * GET TARGET ITEM DATA *
	print("Getting ability data for " + target)
	targetKeywordList = []
	if "Keywords" in targetDict:
		targetKeywordList = [itemKeyword.split("=", 1)[0] for itemKeyword in targetDict['Keywords']]
		print('target keyword list = ' + str(targetKeywordList))

	# * GET ABILITIES DATA
	abilityList = []
	if not targetKeywordList:
		print(target + " has no keywords.")
	else:
		for ability in AbilityDict:
			if "AmmoKeywords" in AbilityDict[ability]:
				for ammoKeyword in AbilityDict[ability]["AmmoKeywords"]:
					if "ItemKeyword" in ammoKeyword:
						if ammoKeyword['ItemKeyword'] in targetKeywordList:
							if "AmmoDescription" in AbilityDict[ability]:
								abDesc = AbilityDict[ability]["AmmoDescription"]
							else:
								abDesc = "Not found"
								print('AmmoDescription not found for' + ability)
							if "AmmoStickChance" in AbilityDict[ability]:
								ammoStickChance = str(int(100 * AbilityDict[ability]['AmmoStickChance'])) + "%"
							else:
								ammoStickChance = "Never"
							if "AmmoConsumeChance" in AbilityDict[ability]:
								ammoConsumeChance = str(int(100 * AbilityDict[ability]['AmmoConsumeChance'])) + "%"
							else:
								ammoConsumeChance = "Always"
							if "Link" in AbilityDict[ability]:
								abName = AbilityDict[ability]['Link']
							else:
								abName = "Not Found"
								print('no link for ' + ability)
							if "IconString" in AbilityDict[ability]:
								abIconString = AbilityDict[ability]['IconString']
							else:
								abIconString = "Not Found"
								print('no iconString for ' + ability)
							if "SkillText" in AbilityDict[ability]:
								abSkill = AbilityDict[ability]['SkillText']
							else:
								abSkill = "Unknown"
								print('no Skill for ' + abName)
							if "Level" in AbilityDict[ability]:
								abLevel = AbilityDict[ability]['Level']
							else:
								abLevel = 666
								print('no Level for ' + abName)
							abilityList.append((abIconString, abName, abDesc, abSkill, abLevel, ammoConsumeChance, ammoStickChance))

	# * SORT ABILITIES DATA AND CONVERT TO STRING
	abilitySource = '====Ability Consumption====\n' + versionString + botInfoString
	if abilityList:
		def getLevel(abilityListElement):
			return abilityListElement[4]

		abilityList.sort(key=getLevel, reverse=False)
		abilitySource += '{| {{STDT|sortable mw-collapsible mw-collapsed}}\n! Icon !! Name !! Consumes !! Skill !! Level !! Consume Chance !! Stick Chance\n'

		def StringifyAbilityTuple(abTuple):  # Ammo consume chance and stick chance already converted to string.
			return ' || '.join((abTuple[0], abTuple[1], abTuple[2], abTuple[3], str(abTuple[4]), abTuple[5], abTuple[6]))

		for abilityTuple in abilityList:
			abilitySource += '|-\n| ' + StringifyAbilityTuple(abilityTuple) + '\n'
		abilitySource += '|}\n'
	else:
		abilitySource += 'None.\n'
	return abilitySource