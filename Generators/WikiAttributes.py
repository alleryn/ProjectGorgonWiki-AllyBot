from .GeneratorGlobalStrings import versionString, botInfoString

def GenerateWikiAttributes(AttributeDict):
	labelsSource = '<noinclude>\n' + versionString + botInfoString + '</noinclude>{{ #if: {{{1|}}} | \n{{ #replace:{{ #switch: {{{1|None}}}\n'
	iconsSource = '<noinclude>\n' + versionString + botInfoString + '</noinclude>{{ #if: {{{1|}}} | \n{{ #replace: http://cdn.projectgorgon.com/__GAMEVERSION__/icons/icon_{{ #switch: {{{1|None}}}\n'

	for attribute in AttributeDict:
		if "Label" in AttributeDict[attribute]:
			labelsSource += '| ' + attribute + ' = ' + AttributeDict[attribute]['Label'] + '\n'
		if "IconIds" in AttributeDict[attribute]:
			iconsSource += '| ' + attribute + ' = ' + str(AttributeDict[attribute]['IconIds'][0]) + '\n'

	labelsSource += '| #default = {{ #if: {{ #pos: {{{1|}}} | : }} |  4003 | <span style="color:red">Error: Attribute not found</span> }}\n}}|\nhttp://cdn.projectgorgon.com/__GAMEVERSION__/icons/icon_<span style="color:red">Error: Attribute not found</span>.png | \n<span style="color:red">Error: Attribute not found</span> }} | [[File:Item-icon-none.png]] }}<noinclude>\n{{Attribute label/Explanation}}\n[[Category:Formatting templates]]\n</noinclude>\n'
	iconsSource += '| #default = {{ #if: {{ #pos: {{{1|}}} | : }} |  4003 | <span style="color:red">Error: Attribute not found</span> }}\n}}.png | \nhttp://cdn.projectgorgon.com/__GAMEVERSION__/icons/icon_<span style="color:red">Error: Attribute not found</span>.png | \n<span style="color:red">Error: Attribute not found</span> }} | [[File:Item-icon-none.png]] }}<noinclude>\n{{Attribute icon/Explanation}}\n[[Category:Formatting templates]]\n</noinclude>\n'

	return labelsSource, iconsSource