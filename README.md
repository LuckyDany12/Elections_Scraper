# Elections Scraper
### Czech Parliament elections 2017 website scraper

This skript will scrape elections data from the official election results website - https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ.

### Libraries

requests, beautifulsoup4, sys, csv

You can find all necessary libraries in requirements.txt
```
pip3 -- version  
pip3 install -r requirements.txt
```

### Running the script

To run the script you have to enter 3 arguments in terminal.
* Name of the file
* Provide URL of choosen territory
Example of the url for Karviná - "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8103"
* Name of the CSV file, where data will be saved.
Example of the CSV file name - karvina.csv

#### Example how to run a skript:
```
python Elections_Scraper.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8103" karvina.csv 
```

#### Data download progress
```
I am downloading data from inserted URL: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8103
Your output is saved in karvina.csv
```

#### Partial outcome
```code,location,registered,envelopes,valid,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Česká národní fronta,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
598925,Albrechtice,3173,1957,1944,109,4,2,181,2,131,211,15,22,12,1,3,139,0,5,25,635,1,1,174,0,10,1,0,255,5
599051,Bohumín,17613,9040,8973,579,12,4,1241,9,133,821,85,91,87,7,6,641,0,12,119,3157,18,33,305,3,55,14,25,1478,38
598933,Český Těšín,19635,10429,10361,698,15,4,877,12,192,760,129,83,107,7,6,828,0,5,214,3597,12,19,1310,3,41,22,16,1365,39
```








