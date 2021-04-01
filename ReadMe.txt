**Summary**:
AllyBot is a bot for generating and maintaining item pages on the Project: Gorgon wiki, located at wiki.projectgorgon.com. For more information, see http://wiki.projectgorgon.com/wiki/User:Alleryn#AllyBot.

**Dependencies**:
- Python, i think i used something out of 3.5 so it should work on any version more recent than that, probably.
- The python package 'requests' must be installed.

**Directory Structure and Files**:
\Archive: Contains old folders from \Jsons moved during JsonCacher.py and old folders from \Data moved during UploadWikiData.py

\Backups: Contains backups of python files created manually by running Backup.py

\Data: Contains various files, including the formatted jsons and the wiki data, generated during the course of running AllyBot. This is in some sense the 'main' folder.

\Generators: Contains the python files that generate the wiki data

\Jsons: Contains the raw wiki data downloaded from cdn.projectgorgon.com by JsonCacher.py

\Logs: log files generated during the course of running AllyBot

**How to Run**:
*After a version update (e.g. 341 -> 342):*
1. Run JsonCacher.py. This fetches the json data from the public server at cdn.projectgorgon.com and copies it locally to \Jsons. And archives (moves) the previous version's json data from \Jsons to \Archive\Jsons. Additionally, in \Jsons (in the subfolder for the new version) the following files are created and you should perform associated tasks:
1a. removedItems.txt : In my experience, usually this file is empty (because no items have been removed). If not, you may wish to add Lore/Trivia info to those items' wiki pages to indicate the items have been removed.
1b. nameChangedItems.txt : Similar to (1a), this case you may want to add Lore/Trivia to the renamed items' wiki pages, but you will first need to manually move the data from the old page to the new one.
1c. addedKeywordsForPython.txt : This is for updating \Generators\WikiGetItemCategoryLink.py You will need to manually enter a reasonable plural form for each keyword.
1d. addedKeywordsForWiki.txt : This is for updating wiki.projectgorgon.com/wiki/Template:ItemCategory
1e. removedKeywords.txt : Like (1a), this usually/always ends up empty. You might want to clean up keywords in the spots where you added keywords in (1c/1d), though this isn't strictly necessary for things to continue functioning (but it would improve efficiency slightly to not have unused keywords in the switch statements).
1f. addedNpcsForNpclocationsJson.txt : This is an important step, even if this file is empty, as it often is.

You will want to copy from the archived jsons folder (e.g. if updating from 341 to 342, we need the file \Archive\Jsons\v341\npclocations.json) and manually copy it to the new jsons folder (e.g. \Jsons\v342). This part could be automated, but i left it manual so that i don't forget to update this file (if i get to step 2 without updating it, the program will know quite early on and not get too far).

Then you will need to add any new npcs' location using addedNpcsForNpclocationsJson.txt and finding out (from players or on your own in-game) where the npcs are located. If you aren't sure, you can just add 'Unknown' as the location.

1g. removedNpcs.txt : Similar to (1e) you might want to clean up npclocations.json with any removed npcs. Sometimes these might include live event npcs like moxie (crafting caravan) who come and go, and it's probably easiest just to leave them in.
1h. addedRecipesForRecipeTemplate.txt : Similar to (1d), you should use this for wiki.projectgorgon.com/wiki/Template:Recipe and wiki.projectgorgon.com/wiki/Template:RecipeToItem
1i. removedRecipes.txt : Similar to (1e).

2. Run FormatJsons.py. This formats the jsons and saves them into \Data (in the subfolder corresponding to the current bot version)
3. Run GenerateWikiData.py. This generates the wiki text that we will later versionize (step 5) and then upload (step 6), skipping over any files that haven't changed since the last version (step 4).
4. Run CompareWikiData.py. This creates a record of which wiki texts have changed since the last version.
5. Run VersionizeWikiData.py. This replaces the placeholder string "__VERSION__" with the version number. (Which was left out to make the comparison step easy). Only wiki texts that have changed since the last version are versionized.
6. Run UploadWikiData.py <username> <password> (without the anglebrackets). You will need to register a bot account with a wiki admin to get a username and password.

If the process is interrupted, the created file CompletedSections.txt contains a list of what has already been uploaded, so that you can simply run UploadWikiData.py again after the bug is fixed to resume operations. If you need to redo any of the already uploaded files, you should manually edit CompletedSections.txt.

After everything uploads successfully, a few cleanup operations happen, archiving the python files and previous version's data, and finally updating botVersion.txt so that AllyBot is ready for next time.

*Or after an update to the bot itself:* Run Backup.py to backup changes to the python code (to \Backups) then do steps 2-6 above.
