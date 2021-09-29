from .GeneratorGlobalStrings import versionString, botInfoString

def GenerateWikiRecipeTemplate(RecipeList, RecipeDict, ItemDict, RecipeSourcesDict):
	templateList = []
	for recipe in RecipeList:
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
				template = ' | ' + recipeName + ' = '
				if len(RecipeDict[recipe]["ResultItems"]) == 1:
					template += ItemDict["item_" + str(RecipeDict[recipe]["ResultItems"][0]["ItemCode"])]["Name"]
				else:
					rItems = []
					for resultItem in RecipeDict[recipe]["ResultItems"]:
						rItems.append(ItemDict["item_" + str(resultItem["ItemCode"])]["Name"])
					if "ProtoResultItems" in RecipeDict[recipe]:
						for protoResultItem in RecipeDict[recipe]["ProtoResultItems"]:
							rItems.append(ItemDict["item_" + str(protoResultItem["ItemCode"])]["Name"])
					template += ' OR '.join(rItems)
				templateList.append(template)
	templateList.sort()
	return '\n'.join(templateList)