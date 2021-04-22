from .GeneratorGlobalStrings import versionString, botInfoString
from .WikiGetItemCategoryLink import getItemCategoryLink

def addRecipe(recipe_, dict_, RecipeDict):
	if "Keywords" in RecipeDict[recipe_] and "Lint_NotLearnable" in RecipeDict[recipe_]["Keywords"]:
		print('Recipe ' + RecipeDict[recipe_]["Name"] + ' is Lint_NotLearnable')
	else:
		print("Working on " + RecipeDict[recipe_]["Name"])
		if not RecipeDict[recipe_]['SkillText'] in dict_:
			recipeSkill = RecipeDict[recipe_]['SkillText']
			dict_[RecipeDict[recipe_]['SkillText']] = [(-1, '{| {{STDT|mw-collapsible mw-collapsed}}\n|+ style="text-align:left; width: 250px;" | ' + recipeSkill + '\n! Lvl !! Name !! Ingredients !! Results\n'), (999, '|}\n')]
		recipeLine = '|-\n| ' + str(RecipeDict[recipe_]['SkillLevelReq']) + ' || ' + RecipeDict[recipe_]['Name'] + ' || '

		ingredientList = []
		for ingredient_ in RecipeDict[recipe_]['Ingredients']:
			if "ItemKeys" in ingredient_:
				category = ingredient_['ItemKeys'][0].replace('EquipmentSlot:', '')
				if ingredient_['StackSize'] > 1:  # Next 5 lines should be replaced with the following line if the error in the cheap meat description fields in recipes.json is fixed
					stackSizeString = ""
				else:
					stackSizeString = ' x1'
				ingredientLine = '[[:Category:Items/' + category + '|' + ingredient_['Desc'] + ']]' + stackSizeString
				# ingredientLine = '[[:Category:Items/' + category + '|' + ingredient_['Desc'] + ']] x' + str(ingredient_['StackSize'])
			elif "ItemCode" in ingredient_:
				ingredientData = ingredient_['IconString'] + '&nbsp;' + ingredient_['Link']
				ingredientLine = ingredientData + ' x' + str(ingredient_['StackSize'])
			else:
				ingredientLine = "Error"
				print('Error. Recipe ' + recipe_ + ' has ingredient ' + ingredient_ + ' with no ItemCode or ItemKeys.')
			if "ChanceToConsume" in ingredient_:
				ingredientLine += ' <span style="display: inline"><sup style="font-weight: bold; color: red;" title="Chance to consume: ' + str(int(100 * ingredient_['ChanceToConsume'])) + '% &#010;">(!)</sup></span>'
			if "ConsumeUses" in ingredient_:
				ingredientLine += ' <span style="display: inline"><sup style="font-weight: bold; color: red;" title="Consumes ' + str(ingredient_['ConsumeUses']) + ' Doses &#010;">(!)</sup></span>'
			ingredientList.append(ingredientLine)

		recipeLine += "<br>".join(ingredientList) + ' || '

		recipeResultsList = []
		for result_ in RecipeDict[recipe_]['ResultItems']:
			resultData = result_['IconString'] + '&nbsp;' + result_['Link']
			resultLine = resultData + ' x' + str(result_['StackSize'])
			if "PercentChance" in result_:
				resultLine += ' <span style="display: inline"><sup style="font-weight: bold; color: red;" title="Chance of being created: ' + str(int(100 * result_['PercentChance'])) + '% &#010;">(!)</sup></span>'
			recipeResultsList.append(resultLine)
		if "ResultString" in RecipeDict[recipe_]:
			recipeResultsList.append(RecipeDict[recipe_]["ResultString"])

		recipeLine += "<br>".join(recipeResultsList) + '\n'

		dict_[RecipeDict[recipe_]['SkillText']].append((RecipeDict[recipe_]['SkillLevelReq'], recipeLine))

# end def addRecipe(recipe_, dict_):

def firstElementOfTuple(x):
	return x[0]

def recipeSort(pair):
	return pair[0]

def getSortedRecipeStringList(dict_):
	for skillKey in dict_:
		dict_[skillKey].sort(key=firstElementOfTuple)  # For each skill, this sorts the list of recipe strings by level
		dict_[skillKey] = ''.join([pair[1] for pair in dict_[skillKey]])  # For each skill, extract the string, discarding the level, and concatenate
	list_ = [(k, v) for k, v in dict_.items()]
	list_.sort(key=recipeSort)
	return [v for (k, v) in list_]  # Sorts the recipe strings alphabetically by skill and extracts the strings, discarding the dictionary key (skill)

def GenerateWikiKeywordRecipeData(keyword, RecipeDict):
	dict = {}
	for recipe in RecipeDict:
		ingredientKeys = []
		for ingredient in RecipeDict[recipe]['Ingredients']:
			if "ItemKeys" in ingredient:
				formattedKey = ingredient['ItemKeys'][0].replace('EquipmentSlot:', '')
				if formattedKey == keyword:
					ingredientKeys.append(formattedKey)
		if ingredientKeys:
			addRecipe(recipe, dict, RecipeDict)
	source = '==Using in Recipes==\n' + versionString + botInfoString
	if dict:
		ingredientRecipeStringList = getSortedRecipeStringList(dict)
		source += ''.join(ingredientRecipeStringList)
	else:
		source += 'None.\n'
	source += '[[Category:Items]]\n'
	return source

def GenerateWikiItemRecipeData(target, targetDict, RecipeDict, keywordSkips):
	# * GET TARGET ITEM DATA *
	print("Getting recipe data for " + target)
	targetCode = target[5:]
	print("Target item code is " + targetCode)

	targetKeywordSet = set()
	genericsSet = set()
	if "Keywords" in targetDict:
		targetKeywordSet = set(itemKeyword.split("=", 1)[0] for itemKeyword in targetDict['Keywords'])
		genericsSet = targetKeywordSet & keywordSkips
		targetKeywordSet = targetKeywordSet - genericsSet
		print('target keyword list = ' + str(targetKeywordSet))

	# * GET RECIPE DATA
	targetIsIngredientRecipeDict = {}
	targetIsResultRecipeDict = {}
	for recipe in RecipeDict:
		ingredientCodes = []
		resultCodes = []
		ingredientKeys = []
		for ingredient in RecipeDict[recipe]['Ingredients']:
			if "ItemKeys" in ingredient:
				formattedKey = ingredient['ItemKeys'][0].replace('EquipmentSlot:', '')
				if formattedKey in targetKeywordSet:
					ingredientKeys.append(formattedKey)
			if "ItemCode" in ingredient:
				if str(ingredient['ItemCode']) == targetCode:
					ingredientCodes.append(ingredient['ItemCode'])
		if ingredientCodes or ingredientKeys:
			addRecipe(recipe, targetIsIngredientRecipeDict, RecipeDict)
		for result in RecipeDict[recipe]['ResultItems']:
			if "ItemCode" in result:
				if str(result['ItemCode']) == targetCode:
					resultCodes.append(result['ItemCode'])
		if resultCodes:
			addRecipe(recipe, targetIsResultRecipeDict, RecipeDict)

	# * SORT AND STRINGIFY RECIPE DATA
	targetIsIngredientRecipeSource = '===Using in Recipes===\n' + versionString + botInfoString
	if targetIsIngredientRecipeDict:
		ingredientRecipeStringList = getSortedRecipeStringList(targetIsIngredientRecipeDict)
		targetIsIngredientRecipeSource += ''.join(ingredientRecipeStringList)
	if genericsSet:
		targetIsIngredientRecipeSource += 'Also can be used in any recipes which call for:\n' + ''.join('*' + getItemCategoryLink(x) + '\n' for x in sorted(genericsSet))
	if not targetIsIngredientRecipeDict and not genericsSet:
		targetIsIngredientRecipeSource += 'None.\n'
	targetIsResultRecipeSource = '===Producing with Recipes===\n' + versionString + botInfoString
	if targetIsResultRecipeDict:
		resultRecipeStringList = getSortedRecipeStringList(targetIsResultRecipeDict)
		targetIsResultRecipeSource += ''.join(resultRecipeStringList)
	else:
		targetIsResultRecipeSource += 'None.\n'
	return targetIsIngredientRecipeSource, targetIsResultRecipeSource