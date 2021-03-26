from .GeneratorGlobalStrings import versionString, botInfoString

def GenerateWikiHardcoreDeathPenaltyItems(ItemDict):
	source = '=== List of Items Usable Only in Hardcore Mode ===\n' + versionString + botInfoString + '<div style="column-count:5;-moz-column-count:5;-webkit-column-count:5">\n'
	for item in ItemDict:
		if "Behaviors" in ItemDict[item]:
			for behavior in ItemDict[item]['Behaviors'][0]:
				if behavior == "UseRequirements":
					if "HardcoreDeathPenalty" in ItemDict[item]['Behaviors'][0]['UseRequirements']:
						source += '*{{Item|' + ItemDict[item]['Name'] + '}}\n'
	source += '</div>'
	return source