import pandas as pd

Dataset = pd.read_excel(
    "D:/Aryan Data/Usefull Data/Semester - 4/Data Visulization and Dashboards/Codes/excel_pivots.xlsx",
    "Orders",
)
print(Dataset)
print(Dataset.shape)
print(Dataset.describe())
print(type(Dataset))
print(Dataset.size)
print(Dataset.columns)

# Que - 1 :- Average "total cost" and count of the product 1 under small order category

Dataframe_1 = Dataset[
    (Dataset["Order_Category"] == "Small Order") & (Dataset["Product_#"] == "Product 1")
]
average_cost_1 = Dataframe_1["Total_Cost"].mean()
Count_1 = Dataframe_1.shape[0]
print(f"Average of Total Cost = $ {average_cost_1}\nCount = {Count_1} for Small Order")

# Que - 2 :- Average "total cost" and count of the product 1 under normal order category

Dataframe_2 = Dataset[
    (Dataset["Order_Category"] == "Normal Order")
    & (Dataset["Product_#"] == "Product 1")
]
average_cost_2 = Dataframe_2["Total_Cost"].mean()
Count_2 = Dataframe_2.shape[0]
print(f"Average of Total Cost = $ {average_cost_2}\nCount = {Count_2} for Normal Order")

# Que - 3 :- Average "total cost" and count of the product 1 under large order category

Dataframe_3 = Dataset[
    (Dataset["Order_Category"] == "Large Order") & (Dataset["Product_#"] == "Product 1")
]
average_cost_3 = Dataframe_3["Total_Cost"].mean()
Count_3 = Dataframe_3.shape[0]
print(f"Average of Total Cost = $ {average_cost_3}\nCount = {Count_3} for Large Order")

# Que - 4 :- Which month is having the highest count of orders placed?

Months = list(set(Dataset["Month"]))
Dictionary = {}

for i in Months:
    Dataframe_4 = Dataset[(Dataset["Month"] == i)]
    Dictionary[i] = Dataframe_4.shape[0]

Dictionary = dict(sorted(Dictionary.items(), key=lambda item: item[1], reverse=True))
highest_count_month = list(Dictionary.keys())[0]
print(
    f"The Month - {highest_count_month} Is Having Highest Count {Dictionary[highest_count_month]}"
)


# Que - 5 :- Which year has the highest "average total cost"?

Years = list(set(Dataset["Year"]))
Year_Dict = {}

for i in Years:
    Dataframe_5 = Dataset[(Dataset["Year"] == i)]
    Average_Cost = sum(Dataframe_5["Total_Cost"]) / Dataframe_5.shape[0]
    Year_Dict[i] = Average_Cost


Year_Dict = dict(sorted(Year_Dict.items(), key=lambda item: item[1], reverse=True))
highest_average_cost_year = list(Year_Dict.keys())[0]
print(
    f"The Year - {highest_average_cost_year} Is Having Highest Average Total Cost - $ {Year_Dict[highest_average_cost_year]}"
)


# Que - 6 :- What is the ratio of the number of orders placed by male and female ?

male_orders = Dataset[Dataset["Gender"] == "Male"].shape[0]
female_orders = Dataset[Dataset["Gender"] == "Female"].shape[0]
ratio = male_orders / female_orders
print(
    f"Number of Orders Placed By Male - {male_orders} and Orders Placed By Female - {female_orders} and The Ratio Is {ratio}"
)


# Que - 7 :- What is the ratio of the total cost of the orders placed by male and female ?

Male_Order = Dataset[(Dataset["Gender"] == "Male")]
Female_Order = Dataset[(Dataset["Gender"] == "Female")]
Total_Male_Cost = sum(Male_Order["Total_Cost"])
Total_Female_Cost = sum(Female_Order["Total_Cost"])
Ratio_of_Total_Cost = Total_Male_Cost / Total_Female_Cost
print(
    f"The Total Cost of Order Placed By Male is $ {Total_Male_Cost} and Total Cost of Order Placed By Female is $ {Total_Female_Cost} and the ration is {Ratio_of_Total_Cost}"
)


# Que - 8 :- How many orders are placed under each order category for the country "INDIA" ?

Category = list(set(Dataset["Order_Category"]))
Category_Dictionary = {}

for i in Category:
    Dataframe_6 = Dataset[
        (Dataset["Country"] == "India") & (Dataset["Order_Category"] == i)
    ]
    Category_Dictionary[i] = Dataframe_6.shape[0]

print(Category_Dictionary)


# Que - 9 :- What is the total cost of order placed by the customer "Willis Brinks"

Dataframe_7 = Dataset[(Dataset["Name"] == "Willis Brinks")]
Total_Cost_Willis_Brinks = sum(Dataframe_7["Total_Cost"])

print(
    f'The Total Cost of Orders Placed By The Customer "Willis Brinks" Is $ {Total_Cost_Willis_Brinks}'
)


# Que - 10 :- Name the customer who has placed the order having the highest amount.

Name = Dataset.loc[Dataset["Total_Cost"] == Dataset["Total_Cost"].max(), "Name"].iloc[0]

print(f"The Name of Person Who has Placed The Order Having the Highest value is {Name}")
