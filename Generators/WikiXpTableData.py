from .GeneratorGlobalStrings import versionString, botInfoString

def GenerateWikiXpTableData(xpTableDict):
	xpTableSource = '<noinclude>' + versionString + botInfoString + '[[Category:Xptable]]</noinclude>\n{| {{STDT}}\n! Level !! Experience !! Total Experience\n'
	totalXp = 0
	for index, xpAmount in enumerate(xpTableDict["XpAmounts"], start=1):
		totalXp += xpAmount
		xpTableSource += '|-\n' + '|' + str(index) + '||' + str(xpAmount) + '||' + str(totalXp) + '\n'
	xpTableSource += '|}\n'
	return xpTableSource
