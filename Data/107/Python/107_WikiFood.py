from .GeneratorGlobalStrings import versionString, botInfoString

def AddToEdibles(ediblesSource, ItemDict, RecipeDict, item, variety, level):
	itemData = ItemDict[item]["IconString"] + '&nbsp;' + ItemDict[item]["Link"]
	foodTypeData = variety
	foodLevelData = level
	recipeTypeData = ''
	recipeLevelData = ''
	for recipe in RecipeDict:
		for result in RecipeDict[recipe]['ResultItems']:
			if "ItemCode" in result:
				if result['ItemCode'] == int(item[5:]):
					recipeTypeData += RecipeDict[recipe]['SkillText']
					recipeLevelData += str(RecipeDict[recipe]['SkillLevelReq'])
	if "SkillReqs" in ItemDict[item] and "Gourmand" in ItemDict[item]["SkillReqs"]:
		gourmandData = str(ItemDict[item]["SkillReqs"]["Gourmand"])
	else:
		gourmandData = str(0)
	ediblesSource += '|-\n| style="text-align:left;" data-sort-value="' + ItemDict[item]["Name"] + '"|' + ' || '.join((itemData, foodTypeData, foodLevelData, recipeTypeData, recipeLevelData, gourmandData)) + '\n'
	return ediblesSource

def GenerateWikiFood(ItemDict, RecipeDict):
	ediblesSource = '=== Edibles ===\n' + versionString + botInfoString + '{| {{STDT|sortable mw-collapsible <includeonly>mw-collapsed</includeonly>}} style="text-align: center"\n! Item !! Food Type !! Food Level !! Recipe Type !! Recipe Level !! Gourmand Requirement\n'
	mealsSource = '=== Meals ===\n' + versionString + botInfoString + '{| {{STDT|sortable mw-collapsible <includeonly>mw-collapsed</includeonly>}} style="text-align: center"\n! Item !! Level !! Gourmand Requirement !! Maximum Health !! Maximum Power !! In-Combat Health Regeneration !! In-Combat Power Regeneration !! Out-of-Combat Health Regeneration !! Out-of-Combat Power Regeneration !! Metabolism Regeneration !! Duration\n'
	snacksSource = '=== Snacks ===\n' + versionString + botInfoString + '{| {{STDT|sortable mw-collapsible <includeonly>mw-collapsed</includeonly>}} style="text-align: center"\n! Item !! Level !! Gourmand Requirement !! Maximum Health !! Maximum Power !! In-Combat Health Regeneration !! In-Combat Power Regeneration !! Out-of-Combat Health Regeneration !! Out-of-Combat Power Regeneration !! Metabolism Regeneration !! Duration\n'
	instantsSource = '=== Instant-Snacks ===\n' + versionString + botInfoString + '{| {{STDT|sortable mw-collapsible <includeonly>mw-collapsed</includeonly>}} style="text-align: center"\n! Item !! Level !! Gourmand Requirement !! Health Restored !! Power Restored !! Metabolism Cost\n'
	for item in ItemDict:
		if "EffectDescs" in ItemDict[item]:
			for effectDesc in ItemDict[item]['EffectDescs']:
				if effectDesc.startswith('Meal Level'):
					ediblesSource = AddToEdibles(ediblesSource, ItemDict,  RecipeDict, item, "Meal", effectDesc[11:])
					mealsSource += '|-\n| style="text-align:left;" data-sort-value="' + ItemDict[item]["Name"] + '"| ' + ItemDict[item]["IconString"] + '&nbsp;' + ItemDict[item]["Link"] + ' || ' + effectDesc[11:] + ' || '
					if "SkillReqs" in ItemDict[item] and "Gourmand" in ItemDict[item]["SkillReqs"]:
						mealsSource += str(ItemDict[item]["SkillReqs"]["Gourmand"])
					else:
						mealsSource += str(0)
					mealsSource += ' || '
					maxHealth = str(0)
					maxPower = str(0)
					inCombatHealthRegen = str(0)
					inCombatPowerRegen = str(0)
					oocHealthRegen = str(0)
					oocPowerRegen = str(0)
					metabolismRegen = str(0)
					duration = str(0)
					for effectDescInner in ItemDict[item]['EffectDescs']:
						if effectDescInner.startswith('Max Health +'):
							maxHealth = effectDescInner[12:]
						elif effectDescInner.startswith('Max Power +'):
							maxPower = effectDescInner[11:]
						elif effectDescInner.startswith('Health Regen +'):
							if effectDescInner.endswith(' per update (in combat)'):
								inCombatHealthRegen = effectDescInner[14:-23]
							else:
								oocHealthRegen = effectDescInner[14:-11]
						elif effectDescInner.startswith('Power Regen +'):
							if effectDescInner.endswith(' per update (in combat)'):
								inCombatPowerRegen = effectDescInner[13:-23]
							else:
								oocPowerRegen = effectDescInner[13:-11]
						elif effectDescInner.startswith('Metabolism Regen +'):
							metabolismRegen = effectDescInner[18:-11]
						elif effectDescInner.startswith('Lasts '):
							duration = effectDescInner[6:-22]
					mealsSource += maxHealth + ' || ' + maxPower + ' || ' + inCombatHealthRegen + ' || ' + inCombatPowerRegen + ' || ' + oocHealthRegen + ' || ' + oocPowerRegen + ' || ' + metabolismRegen + ' || ' + duration + '\n'
				elif effectDesc.startswith('Snack Level'):
					ediblesSource = AddToEdibles(ediblesSource, ItemDict, RecipeDict, item, "Snack", effectDesc[12:])
					snacksSource += '|-\n| style="text-align:left;" data-sort-value="' + ItemDict[item]["Name"] + '"| ' + ItemDict[item]["IconString"] + '&nbsp;' + ItemDict[item]["Link"] + ' || ' + effectDesc[12:] + ' || '
					if "SkillReqs" in ItemDict[item] and "Gourmand" in ItemDict[item]["SkillReqs"]:
						snacksSource += str(ItemDict[item]["SkillReqs"]["Gourmand"])
					else:
						snacksSource += str(0)
					snacksSource += ' || '
					maxHealth = str(0)
					maxPower = str(0)
					inCombatHealthRegen = str(0)
					inCombatPowerRegen = str(0)
					oocHealthRegen = str(0)
					oocPowerRegen = str(0)
					metabolismRegen = str(0)
					duration = str(0)
					for effectDescInner in ItemDict[item]['EffectDescs']:
						if effectDescInner.startswith('Max Health +'):
							maxHealth = effectDescInner[12:]
						elif effectDescInner.startswith('Max Power +'):
							maxPower = effectDescInner[11:]
						elif effectDescInner.startswith('Health Regen +'):
							if effectDescInner.endswith(' per update (in combat)'):
								inCombatHealthRegen = effectDescInner[14:-23]
							else:
								oocHealthRegen = effectDescInner[14:-11]
						elif effectDescInner.startswith('Power Regen +'):
							if effectDescInner.endswith(' per update (in combat)'):
								inCombatPowerRegen = effectDescInner[13:-23]
							else:
								oocPowerRegen = effectDescInner[13:-11]
						elif effectDescInner.startswith('Metabolism Regen +'):
							metabolismRegen = effectDescInner[18:-11]
						elif effectDescInner.startswith('Lasts '):
							duration = effectDescInner[6:-22]
					snacksSource += maxHealth + ' || ' + maxPower + ' || ' + inCombatHealthRegen + ' || ' + inCombatPowerRegen + ' || ' + oocHealthRegen + ' || ' + oocPowerRegen + ' || ' + metabolismRegen + ' || ' + duration + '\n'
				elif effectDesc.startswith('Instant-Snack Level'):
					ediblesSource = AddToEdibles(ediblesSource, ItemDict, RecipeDict, item, "Instant-Snack", effectDesc[20:])
					instantsSource += '|-\n| style="text-align:left;" data-sort-value="' + ItemDict[item]["Name"] + '"| ' + ItemDict[item]["IconString"] + '&nbsp;' + ItemDict[item]["Link"] + ' || ' + effectDesc[20:] + ' || '
					if "SkillReqs" in ItemDict[item] and "Gourmand" in ItemDict[item]["SkillReqs"]:
						instantsSource += str(ItemDict[item]["SkillReqs"]["Gourmand"])
					else:
						instantsSource += str(0)
					instantsSource += ' || '
					health = str(0)
					power = str(0)
					metabolismCost = str(0)
					for effectDescInner in ItemDict[item]['EffectDescs']:
						if effectDescInner.startswith('Restores '):
							if effectDescInner.endswith(' health'):
								health = effectDescInner[9:-7]
							elif effectDescInner.endswith(' power'):
								power = effectDescInner[9:-6]
					if "Behaviors" in ItemDict[item]:
						for behavior in ItemDict[item]["Behaviors"]:
							if "MetabolismCost" in behavior:
								metabolismCost = str(behavior["MetabolismCost"])
					instantsSource += health + ' || ' + power + ' || ' + metabolismCost + '\n'

	mealsSource += '|}\n'
	snacksSource += '|}\n'
	instantsSource += '|}\n'
	ediblesSource += '|}\n'
	return ediblesSource, mealsSource, snacksSource, instantsSource