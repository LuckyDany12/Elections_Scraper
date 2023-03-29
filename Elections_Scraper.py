"""
Elections_Scraper.py: Third project in Engeto online python academy
Author: Daniela Horucková
Email: horuckova.d@seznam.cz
Discord: LuckyDany#2774
"""

import requests
from bs4 import BeautifulSoup
import sys 
import csv


def get_rows(url: str) -> list:
    """Function will get all the rows from the table from the url."""
    print(f"I am downloading data from inserted URL: {url}")
    tables = BeautifulSoup(requests.get(url).text, 'html.parser').find_all\
    ("table", {"class": "table"})
    all_rows = [row for table in tables for row in table.find_all("tr")[2:]]
    return all_rows


def get_code_location(all_rows: list) -> tuple:
    """Function will get the code and location from the table."""
    code = [row.find_all("td")[0].text for row in all_rows
            if row.find_all("td")[0].text != "-"]
    location = [row.find_all("td")[1].text for row in all_rows
                if row.find_all("td")[1].text != "-"]
    return code, location


def tables_detail(all_rows: list) -> tuple:
    """Function will scrape sub URL and will get data of two tables."""
    base_url = "https://www.volby.cz/pls/ps2017nss/"
    tab_district, tab_vote = [], []
    links = [base_url + row.find("a", href=True)["href"] for row in all_rows
             if row.find("a", href=True) is not None]
    for link in links:
        soup = BeautifulSoup(requests.get(link).text, 'html.parser')
        tab_district.append(soup.find_all("table", {"class": "table"})[0])
        tab_vote.extend(soup.find_all("table", {"class": "table"})[1:3])
    return tab_district, tab_vote


def get_votes(tab_district: list) -> tuple:
    """Function will get the nubers of registered voters, 
    number of envelopes and how many votes were valid from the first table."""
    register = [tab.find("td",{"class": "cislo", "data-rel": "L1",
                         "headers": "sa2"}).text.replace("\xa0","") 
                         for tab in tab_district]
    envelope = [tab.find("td", {"class": "cislo", "data-rel": "L1",
                         "headers": "sa3"}).text.replace("\xa0","") 
                         for tab in tab_district]
    valid = [tab.find("td", {"class": "cislo", "data-rel": "L1",
                         "headers": "sa6"}).text.replace("\xa0","") 
                         for tab in tab_district]
    return register, envelope, valid


def get_head(tab_vote: list) -> list:
    """Function will get the head of the second table."""
    head = [tr.find("td", {"class": "overflow_name"}).text 
            for tr in tab_vote[0].find_all("tr")[2:len(tab_vote[0])]]
    head.extend([tr.find("td", {"class": "overflow_name"}).text 
                 for tr in tab_vote[1].find_all("tr")[2:len(tab_vote[1])]])
    return head


def results(tab_vote: list) -> list:
    """Function will return data about numbers of valid votes 
    for individual parties."""
    result_1 = []
    result_2 = []
    for rows in tab_vote:
        value_1 = rows.find_all("td", {"class": "cislo", 
                                       "headers": "t1sa2 t1sb3"})
        value_2 = rows.find_all("td", {"class": "cislo", 
                                       "headers": "t2sa2 t2sb3"})
        values_1 = [v.text.replace("\xa0", "") for v in value_1]
        values_2 = [v.text.replace("\xa0", "") for v in value_2]
        if values_1:
            result_1.append(values_1)
        if values_2:
            result_2.append(values_2)
    final_list = list(zip(*result_1)) + list(zip(*result_2))
    return final_list


def create_dict(head: list, final_list: list) -> dict:
    """Function will create a dictionary with the name of the parties as keys
      and numbers of votes as values."""
    dict_vote = {}
    for i, party in enumerate(head):
        dict_vote[party] = final_list[i]
    return dict_vote


def scrape_url(url: str) -> dict:
    """Function will scrape the url and return all data needed for output."""
    all_rows = get_rows(url)
    tab_district, tab_vote = tables_detail(all_rows)
    code, location = get_code_location(all_rows)
    register, envelope, valid = get_votes(tab_district)
    dict_vote = create_dict(get_head(tab_vote), results(tab_vote))
    data_all = {"code":code, "location": location, "registered": register,
                "envelopes": envelope, "valid": valid,}
    data_all.update(dict_vote)
    return data_all


def save_to_csv(file_name: str, data_all: dict):
    """Function will save data to CSV file."""
    with open(file_name, mode='w', newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(data_all.keys())
        writer.writerows(zip(*data_all.values()))


def main():
    """Function will start the program."""
    if len(sys.argv) != 3:
        print("You must input 3 arguments in to the terminal\
(Name of the main file, URL of the website, Name of final CSV file)")
    else:
        url = sys.argv[1]
        csv = sys.argv[2]
        save_to_csv(csv, scrape_url(url))
        print(f"Your output is saved in {csv}")
    

if __name__ == "__main__":
    main()  


# url = "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8103"
# csv = output.csv
