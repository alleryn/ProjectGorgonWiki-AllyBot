from .GeneratorGlobalStrings import versionString, botInfoString
from .WikiGetItemCategoryLink import getItemCategoryLink

def GenerateWikiItemFavorData(target, targetDict, NpcDict):

	def getKeywordVal(keyword):
		for kw_ in targetDict['Keywords']:
			kws = kw_.split("=", 1)
			if kws[0] == keyword:
				if len(kws) == 2:
					return kws[1]
				else:
					return None

	# * GET TARGET ITEM DATA *
	print("Getting favor data for " + target)
	targetKeywordSet = set()
	if "Keywords" in targetDict:
		targetKeywordSet = set(itemKeyword.split("=", 1)[0] for itemKeyword in targetDict['Keywords'])
		print('target keyword list = ' + str(targetKeywordSet))
	if targetDict["Value"] == 0:
		targetKeywordSet = set(x for x in targetKeywordSet if getKeywordVal(x) is not None)

	# * GET AND SORT FAVOR DATA
	npcPrefList = []  # A list. Each element is a tuple of the form ( npc name, location name, preference-dictionary list ) where preference-dictionary list is a list of the npc's preferences
	# for the item in question. This preference-dictionary list is a list instead of a single value, as the npc may have multiple preferences for a single item based on various
	# keywords (e.g. the npc may like keyword1, but hate keyword2).
	if targetKeywordSet:
		for npc in NpcDict:
			prefList = []
			if 'Preferences' in NpcDict[npc]:
				for preference in NpcDict[npc]['Preferences']:
					preference['Keywords'] = [keyword.replace('EquipmentSlot:', '') for keyword in preference['Keywords']]  # Should happen in FormatJsons
					if set(preference['Keywords']).issubset(set(targetKeywordSet)):
						prefList.append(preference)
			if prefList:
				npcPrefList.append((NpcDict[npc]["Link"], NpcDict[npc]["Location"], prefList))
		if npcPrefList:
			def npcPrefSortOrder(npcPrefListElement):  # Takes an npc preference list element and assigns it a sort value, determined by its preference magnitude list.  A magList with a single magnitude has that value.
				# A magList with multiple postive magnitudes is assigned highest magnitude; a magList with multiple negative mags is assigned lowest;
				# and a magList with conflicted magnitudes is assigned zero.
				pList = npcPrefListElement[2]
				magList = [p["Pref"] for p in pList]
				if len(magList) == 1:
					return magList[0]
				elif all(mag > 0 for mag in magList):
					return max(magList)
				elif all(mag < 0 for mag in magList):
					return min(magList)
				else:
					return 0

			npcPrefList.sort(key=npcPrefSortOrder, reverse=True)
		else:
			print(target + " has keywords, but no NPC has any feelings about them.")

	# *  CONVERT FAVOR DATA TO STRING
	favorSource = '===Gifting===\n' + versionString + botInfoString
	if npcPrefList:

		def prefMagText(mag):
			if mag <= -2:
				return 'Hates'
			elif mag <= -1:
				return 'Dislikes'
			elif mag < 1:
				print("ERROR. Preference magnitude between -1 and 1 detected.  Unsure what text these values take, as they were conjectured not to exist")
			elif mag <= 2:
				return 'Likes'
			else:
				return 'Loves'

		def color(npTuple):
			if npcPrefSortOrder(npTuple) <= -2:
				return 'style="background:#F24A4A;"'
			elif npcPrefSortOrder(npTuple) <= -1:
				return 'style="background:#F29E4A;"'
			elif npcPrefSortOrder(npTuple) < 1:
				return 'style="background:#F2F24A;"'
			elif npcPrefSortOrder(npTuple) <= 2:
				return 'style="background:#9EF24A;"'
			else:
				return 'style="background:#4AF24A;"'

		favorSource += '{| {{STDT|mw-collapsible mw-collapsed}}\n! NPC !! Location !! Preferences\n'
		keywordFlag = False
		for npcPreferenceTuple in npcPrefList:
			prefList = npcPreferenceTuple[2]
			prefTextList = []
			for pref in prefList:
				prefKeywordList = pref["Keywords"]
				prefKeywordTextList = []
				for keyword in prefKeywordList:
					if getKeywordVal(keyword) is None:
						prefKeywordTextList.append(getItemCategoryLink(keyword))
					else:
						keywordFlag = True
						prefKeywordTextList.append(getItemCategoryLink(keyword) + ' : ' + getKeywordVal(keyword) + '*')
				prefKeywordText = ' (' + ' and '.join(prefKeywordTextList) + ')'
				prefTextList.append(prefMagText(pref["Pref"]) + prefKeywordText)
			prefText = '<br>'.join(prefTextList)
			favorSource += '|- ' + color(npcPreferenceTuple) + '\n| ' + npcPreferenceTuple[0] + ' || ' + npcPreferenceTuple[1] + ' || ' + prefText + '\n'
		favorSource += '|}\n'
		if keywordFlag:
			favorSource += '<nowiki>*</nowiki>' + targetDict["Link"] + ' has an effective value different from its base value (' + str(targetDict["Value"]) + ') when gifted as a member of this item category.'
	else:
		favorSource += 'None.\n'
	return favorSource
