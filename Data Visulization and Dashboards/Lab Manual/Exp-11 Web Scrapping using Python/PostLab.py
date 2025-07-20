import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_India"
Page = requests.get(url)

Soup = BeautifulSoup(Page.text, "html")
Table = Soup.find_all("table")

Table = Table[0]

Headers = Table.find_all("th")
Titles = [titles.text.strip() for titles in Headers]

Dataset = pd.DataFrame(columns=Titles)
Rows = Table.find_all("tr")

for row in Rows[1:]:
    Data = row.find_all("td")
    Data_filtered = [Data[i] for i in range(len(Data)) if i not in [1, 3]]
    Row_Data = [row.text.strip() for row in Data_filtered]
    Dataset.loc[len(Dataset)] = Row_Data

Dataset.to_excel("D:/Aryan Data/Usefull Data/Semester - 4/Data Visulization and Dashboards/Lab Manual/Exp-11 Web Scrapping using Python/Largest Companies In India.xlsx",index=False,)
# print("File Saved")


Dataset["Revenue(billions US$)"] = Dataset["Revenue(billions US$)"].astype(str)
Dataset["Revenue(billions US$)"] = (
    Dataset["Revenue(billions US$)"].str.replace(",", "").astype(float)
)

total_revenue = Dataset["Revenue(billions US$)"].sum()
Market_Share = {"Company_Name": [], "Share": []}

for index, row in Dataset.iterrows():
    company_name = row["Name"]
    revenue = row["Revenue(billions US$)"]
    share_percentage = (revenue / total_revenue) * 100
    Market_Share["Company_Name"].append(company_name)
    Market_Share["Share"].append(f"{share_percentage:.2f} %")

Market_Share = pd.DataFrame(Market_Share)
# print(Market_Share)

Industry = Dataset.groupby("Industry")["Name"].unique()
# print(Industry)

Headquarters = Dataset.groupby("Headquarters")["Name"].unique()
print(Headquarters)
