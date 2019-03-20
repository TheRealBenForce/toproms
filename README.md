# toproms
The goal of this repo is to trim large rom collections into only the most 
popular for each console. This is not functional at the moment and still in early development.

I plan to collect rom lists using the IGDB api and sorted by the "popularity"
attribute and compare it to existing rom collections. This will be fun too
because I get to experiment with fuzzy searching.

## project goals
### short term
- Searches a director for rom folders and makes a new folder of the 50 most popular roms


### long term
- Support for japanese roms
- Different dimensions such as rating
- More than 50 games
- Best guess at all roms in a series


## personal goals
- improve my OOP
- Experiment use fuzzy searching
- Learn postman
- Use a real logging module


## To Do
- Argparse to pass a paid api key and get more than 200 results back
- Parameterize how many roms you want either by count or size on disk
- Parameterize threshold to match a game
