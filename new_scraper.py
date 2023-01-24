from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
import csv

start_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

browser = webdriver.Chrome("G:/game/Python/class activity/class 127/chromedriver.exe")
browser.get(start_url)

time.sleep(10)

new_planets_data = []

def more_scrape_data(hyperlink):
    headers = ["brown_dwarf","constellation","right_ascension","declination","app_mag","distance","spectral_type","mass","radius","discovery_year"]
    planets_data = []
    try:
        page = requests.get(hyperlink)
        soup = BeautifulSoup(page.content,"html.parser")
        temp_list = []
        for tr_tags in soup.find_all("tr", attrs={"class","wikitable"}):
            td_tags = tr_tags.find_all("td")
            for td_tag in td_tags:
                try:
                    temp_list.append(td_tag.find_all("div",attrs = {"class":"value"})[0].contents[0])
                except:
                    temp_list.append("")
        new_planets_data.append(temp_list)
    except:
        time.sleep(1)
        more_scrape_data(hyperlink)

    with open("new_scraped_data.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planets_data)

planet_df_1 = pd.read_csv("scraped_data.csv")

scraped_data = []

for row in new_planets_data:
    replaced=[]

    for el in row:
        el = el.replace('\n',"")
        replaced.append(el)
    scraped_data.append(replaced)

print(scraped_data)

headers = ["brown_dwarf","constellation","right_ascension","declination","app_mag","distance","spectral_type","mass","radius","discovery_year"]
new_planet_df_1 = pd.DataFrame(scraped_data, columns = headers)

new_planet_df_1.to_csv("new_scraped_data.csv", index = True, index_label="id")