# Elections Scraper
### Czech Parliament elections 2017 website scraper

#### This skript will scrape elections data from the official election results website - https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ.

### Libraries
#### requests, beautifulsoup4, sys, csv
#### You can find all necessary libraries in requirements.txt\ ```pip3 install -r requirements.txt```

### Running the script
#### To run the script you have to enter 3 arguments in terminal.\ - First is name of the file\ - For second argument you have to choose the territory and provide URL.\ Example of the url for Karviná - "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8103"
#### In to the second argument you should type name of the CSV file where data will be saved.\ Example of the CSV file name - karvina.csv

#### Example how to run a skript:\ ```python Elections_Scraper.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8103" karvina.csv ```










