# toproms
The goal of this repo is to trim large rom collections into only the most 
popular for each console. This is not functional at the moment and still in early development.

I plan to collect rom lists using the IGDB api and sorted by the "popularity"
attribute and compare it to existing rom collections. This will be fun too
because I get to experiment with fuzzy searching.

## How to use
1. Download and unzip repository
2. Install python modules
    * pip install pyyaml requests fuzzywuzzy
    * Optionally python-Levenshtein to make things go a lot quicker. You will also need [Microsoft Visual C++ Compiler for Python 2.7](http://aka.ms/vcpython27).
3. Edit config.csv to point to your rom folders. If you have an unreferenced platform, you can look it up in yamls\platform_list.yml
4. run 'python \_\_main__.py'. The program will take a best guess to make a subset of your highest rated roms and copy to toproms folder.
    * To refresh the platform and top rates game list, optionally, run 'python \_\_main__.py -a IGDB', where IGDB is an IGDB api key.
5. Logging will be reported to 'info.log' and 'errors.log'. Please report any bugs and I will try to fix.

## About how matching works
This may need tuning overtime, but this is how it work. Open to suggestions:

1. First for a given platform, I collected a list of all games with at least 5 ratings from IGDB.
2. Then in descending order by total rating, I print the list. Right now the limit is 150 games due to using a free API.
3. A file list is read in. The extension is extracted and anything at the end of the string inside () or [].
4. A python module that does fuzzy search compares each game in the IGDB list looking for the top score from your collection.
    I found games below ~80 or 85 to not be worth of inclusion so I drop these.
5. The highest scored game from your collection is later copied to a new folder.

## project goals
### short term
- Searches a director for rom folders and makes a new folder of the 50 most popular roms


### long term
- Support for japanese roms
- Different dimensions such as rating
- More than 150 games
- Best guess at all roms in a series
- publish to pypi


## personal goals
- improve my OOP
- Experiment use fuzzy searching
- Learn postman


## To Do
- Argparse to pass a paid api key and get more than 200 results back
- Parameterize how many roms you want either by count or size on disk
- Parameterize score threshold to match a game
- Move get_console_name to the platforms module 
- Fix Dragon Quest / Dragon Warrior type problems
- Remove common words to improve search scoring (ie, Legend of Zelda vs The Legend of Zelda)
- rework objects
- Fix writing yaml files if subfolder doesn't exist