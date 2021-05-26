from .GeneratorGlobalStrings import versionString, botInfoString

def GenerateWikiRecipeTemplate(RecipeDict, ItemDict, RecipeSourcesDict):
	recipeTemplateSource = '<noinclude>\n' + versionString + '</noinclude><includeonly>{{#switch: {{{1|}}}\n'
	for recipe in RecipeDict:
		if "Keywords" in RecipeDict[recipe] and ("Lint_NotLearnable" in RecipeDict[recipe]["Keywords"] or "Lint_NotObtainable" in RecipeDict[recipe]["Keywords"]):
			continue
		automaticFromSkill = True
		for acquisition in RecipeSourcesDict[recipe]:
			if acquisition["Type"] != "AutomaticFromSkill":
				automaticFromSkill = False
		if not automaticFromSkill:
			recipeName = RecipeDict[recipe]["Name"]
			sameName = False
			if "ResultItems" in RecipeDict[recipe]:
				for resultItem in RecipeDict[recipe]["ResultItems"]:
					if ItemDict["item_" + str(resultItem["ItemCode"])]["Name"] == recipeName:
						sameName = True
			if not sameName:
				recipeTemplateSource += ' | ' + recipeName + ' = '
				if len(RecipeDict[recipe]["ResultItems"]) == 1:
					recipeTemplateSource += ItemDict["item_" + str(RecipeDict[recipe]["ResultItems"][0]["ItemCode"])]["Name"] + '\n'
				else:
					recipeTemplateSource += '<noinclude><!-- ' + recipe + ': ' + recipeName + 'produces the following result items: '
					rItems = []
					for resultItem in RecipeDict[recipe]["ResultItems"]:
						rItems.append(ItemDict["item_" + str(resultItem["ItemCode"])]["Name"])
					recipeTemplateSource += ', '.join(rItems) + '. Manually edit out the noinclude and comment tags and pick one result item for this template to display.--></noinclude>' + '\n'
	recipeTemplateSource += ' | #default = {{{1}}}}}</includeonly><noinclude>\n{{documentation}}\n[[Category:Formatting templates]]\n</noinclude>\n'
	return recipeTemplateSource