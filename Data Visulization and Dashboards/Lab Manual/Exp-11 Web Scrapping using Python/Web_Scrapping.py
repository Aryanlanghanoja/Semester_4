  # import pandas as pd
# import requests
# from bs4 import BeautifulSoup

# url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
# Page = requests.get(url)
# Soup = BeautifulSoup(Page.text,"html")
# Table = Soup.find_all("table")
# Table = Table[1]
# Headers = Table.find_all("th")
# Titles = [titles.text.strip() for titles in Headers]
# Dataset = pd.DataFrame(columns = Titles)

# Rows = Table.find_all('tr')

# for row in Rows[1:] :
#   Data = row.find_all('td')
#   Row_Data = [row.text.strip() for row in Data]
#   length = len(Dataset)
#   Dataset.loc[length] = Row_Data

# print(Dataset)
# Dataset.to_excel("D:/Aryan Data/Usefull Data/Semester - 4/Data Visulization and Dashboards/Lab/Web Scrapping/Largest Companies In USA by Revenue.xlsx",index=False)
# print("File Saved")

import pandas as pd
from selenium import webdriver

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_India"
driver = webdriver.Chrome()
driver.get(url)

table = driver.find_elements("xpath" , "//table")[0]
headers = table.find_elements("xpath", ".//th")
titles = [header.text.strip() for header in headers]

dataset = pd.DataFrame(columns=titles)

rows = table.find_elements("xpath"  ,".//tr")[1:]

for row in rows:
    data = row.find_elements("xpath"  , ".//td")
    row_data = [cell.text.strip() for cell in data]
    dataset.loc[len(dataset)] = row_data

print(dataset)
dataset.to_excel("D:/Aryan Data/Usefull Data/Semester - 4/Data Visulization and Dashboards/Lab Manual/Exp-11 Web Scrapping Using Python/Largest Companies In India by Revenue by selenium.xlsx", index=False)
print("File Saved")

driver.quit()
