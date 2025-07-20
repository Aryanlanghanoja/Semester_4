import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
Page = requests.get(url)

Soup = BeautifulSoup(Page.text, "html")
Table = Soup.find_all("table")
Table = Table[1]

Headers = Table.find_all("th")
Titles = [titles.text.strip() for titles in Headers]

Dataset = pd.DataFrame(columns=Titles)
Rows = Table.find_all("tr")

for row in Rows[1:]:
    Data = row.find_all("td")
    Row_Data = [row.text.strip() for row in Data]
    length = len(Dataset)
    Dataset.loc[length] = Row_Data

Dataset.to_excel("D:/Aryan Data/Usefull Data/Semester - 4/Data Visulization and Dashboards/Lab/Web Scrapping/Largest Companies In USA by Revenue.xlsx",index=False,)
# print("File Saved")

Dataset["Revenue (USD millions)"] = (
    Dataset["Revenue (USD millions)"].str.replace(",", "").astype(float)
)

total_revenue = Dataset["Revenue (USD millions)"].sum()
Market_Share = {"Company_Name": [], "Share": []}

for index, row in Dataset.iterrows():
    company_name = row["Name"]
    revenue = row["Revenue (USD millions)"]
    share_percentage = (revenue / total_revenue) * 100
    Market_Share["Company_Name"].append(company_name)
    Market_Share["Share"].append(share_percentage)

Market_Share = pd.DataFrame(Market_Share)
Market_Share["Share"] = Market_Share["Share"].map("{:.2f}%".format)
# print(Market_Share)

Industry = Dataset.groupby("Industry")["Name"].unique()
# print(Industry)

Headquarters = Dataset.groupby("Headquarters")["Name"].unique()
print(Headquarters)
