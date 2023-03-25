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


def get_rows(url):
    print(f"I am downloading data from inserted URL: {url}")
    tables = BeautifulSoup(requests.get(url).text, 'html.parser').\
        find_all("table", {"class": "table"})
    all_rows = [row for table in tables for row in table.find_all("tr")[2:]]
    return all_rows
    

def get_code_location(all_rows):
    code = [row.find_all("td")[0].text for row in all_rows \
            if row.find_all("td")[0].text != "-"]
    location = [row.find_all("td")[1].text for row in all_rows \
                if row.find_all("td")[1].text != "-"]
    return code, location


def tables_detail(all_rows):
    base_url = "https://www.volby.cz/pls/ps2017nss/"
    tab_district, tab_vote = [], []
    links = [base_url + row.find("a", href=True)["href"] for row in all_rows \
             if row.find("a", href=True) is not None]
    for link in links:
        soup = BeautifulSoup(requests.get(link).text, 'html.parser')
        tab_district.append(soup.find_all("table", {"class": "table"})[0])
        tab_vote.extend(soup.find_all("table", {"class": "table"})[1:3])
    return tab_district, tab_vote


def get_votes(tab_district):
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


def get_head(tab_vote):
    head = [tr.find("td", {"class": "overflow_name"}).text \
            for tr in tab_vote[0].find_all("tr")[2:len(tab_vote[0])]]
    head.extend([tr.find("td", {"class": "overflow_name"}).text \
                 for tr in tab_vote[1].find_all("tr")[2:len(tab_vote[1])]])
    return head


def votes_values(rows, class_val, header_val):
    value = rows.find_all("td", {"class": class_val, "headers": header_val})
    return [v.text.replace("\xa0", "") for v in value]

def results(tables_vote):
    result_1 = [votes_values(rows, "cislo", "t1sa2 t1sb3") \
                for rows in tables_vote]
    result_2 = [votes_values(rows, "cislo", "t2sa2 t2sb3") \
                for rows in tables_vote]
    list_1 = list(zip(*[r for r in result_1 if r]))
    list_2 = list(zip(*[r for r in result_2 if r]))
    final_list = list_1 + list_2
    return final_list


def create_dict(head, final_list):
    dict_vote = {}
    for i, party in enumerate(head):
        dict_vote[party] = final_list[i]
    return dict_vote

def scrape_url(url):
    all_rows = get_rows(url)
    tab_district, tab_vote = tables_detail(all_rows)
    code, location = get_code_location(all_rows)
    register, envelope, valid = get_votes(tab_district)
    dict_vote = create_dict(get_head(tab_vote), results(tab_vote))
    data_all = {"code":code, "location": location, "registered": register, \
                "envelopes": envelope, "valid": valid,}
    data_all.update(dict_vote)
    return data_all

def save_to_csv(file_name, data_all):
    with open(file_name, mode='w', newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(data_all.keys())
        writer.writerows(zip(*data_all.values()))

def main():
    if len(sys.argv) != 3:
        print("You must input 3 arguments in to terminal\
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
