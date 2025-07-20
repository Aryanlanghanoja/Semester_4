import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
Page = requests.get(url)
Soup = BeautifulSoup(Page.text,"html")
Table = Soup.find_all("table")
Table = Table[1]
Headers = Table.find_all("th")
Titles = [titles.text.strip() for titles in Headers]
Dataset = pd.DataFrame(columns = Titles)

Rows = Table.find_all('tr')

for row in Rows[1:] :
  Data = row.find_all('td')
  Row_Data = [row.text.strip() for row in Data]
  length = len(Dataset)
  Dataset.loc[length] = Row_Data

print(Dataset)
Dataset.to_excel("D:/Aryan Data/Usefull Data/Semester - 4/Data Visulization and Dashboards/Lab/Web Scrapping/Largest Companies In USA by Revenue.xlsx",index=False)
print("File Saved")