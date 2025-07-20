import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Importing necessary libraries

# Reading the dataset
Dataset = pd.read_excel("D:/Aryan Data/Usefull Data/Semester - 4/Data Visulization and Dashboards/Assigments/Assignment 4 working over Python/excel_pivots.xlsx","Orders")

# Converting Order_Date column to datetime
Dataset["Order_Date"] = pd.to_datetime(Dataset["Order_Date"])

# Extracting Year, Quarter, and Month from Order_Date
Dataset["Year"] = Dataset["Order_Date"].dt.year
Dataset["Quater"] = Dataset["Order_Date"].dt.quarter
Dataset["Month"] = Dataset["Order_Date"].dt.month

# Question - 1: Average "total cost" and count of product 1 under normal order category
Order_With_Normal_Category_of_Product_1 = Dataset[(Dataset["Order_Category"] == "Normal Order") & (Dataset["Product_#"] == "Product 1")]

Count_of_Order_With_Normal_Category_of_Product_1 = Order_With_Normal_Category_of_Product_1.shape[0]
Average_Total_Cost_of_Order_With_Normal_Category_of_Product_1 = Order_With_Normal_Category_of_Product_1["Total_Cost"].mean()

print(f"Answer - 1)\nThe Average Total Cost For Product 1 In Normal Category Is $ {Average_Total_Cost_of_Order_With_Normal_Category_of_Product_1} and the Count of Orders are {Count_of_Order_With_Normal_Category_of_Product_1}.")

# Question - 2: Average "total cost" and count of product 1 under short order category
Order_With_Small_Category_of_Product_1 = Dataset[(Dataset["Order_Category"] == "Small Order") & (Dataset["Product_#"] == "Product 1")]

Count_of_Order_With_Small_Category_of_Product_1 = Order_With_Small_Category_of_Product_1.shape[0]
Average_Total_Cost_Order_With_Small_Category_of_Product_1 = Order_With_Small_Category_of_Product_1["Total_Cost"].mean()

print(f"Answer - 2)\nThe Average Total Cost For Product 1 In Short Category Is $ {Average_Total_Cost_Order_With_Small_Category_of_Product_1} and the Count of Orders are {Count_of_Order_With_Small_Category_of_Product_1}.")

# Question - 3: Average "total cost" and count of product 1 under large order category
Order_With_Large_Category_of_Product_1 = Dataset[(Dataset["Order_Category"] == "Large Order") & (Dataset["Product_#"] == "Product 1")]

Count_of_Order_With_Large_Category_of_Product_1 = Order_With_Large_Category_of_Product_1.shape[0]
Average_Total_Cost_Order_With_Large_Category_of_Product_1 = Order_With_Large_Category_of_Product_1["Total_Cost"].mean()

print(f"Answer - 3)\nThe Average Total Cost For Product 1 In Large Category Is $ {Average_Total_Cost_Order_With_Large_Category_of_Product_1} and the Count of Orders are {Count_of_Order_With_Large_Category_of_Product_1}.")

# Question - 4: Which month has the highest count of orders placed?
Month_Having_Highest_Count = Dataset["Month"].mode()[0]
print(f"Answer - 4)\nThe {Month_Having_Highest_Count}th Month Has the Highest Count of Orders.")

# Question - 5: Which year has the highest "average total cost"?
Year_Wise_Average_Total_Cost = Dataset.groupby("Year")["Total_Cost"].mean()
Year_Having_Highest_Average_Total_Cost = Year_Wise_Average_Total_Cost.idxmax()
print(f"Answer - 5)\nThe Year - {Year_Having_Highest_Average_Total_Cost} Has The Highest Average Total Cost.")

# Question - 6: What is the ratio of the number of orders placed by male and female?
Orders_Given_By_Male_Customers = Dataset[(Dataset["Gender"] == "Male")]
Orders_Given_By_Female_Customers = Dataset[(Dataset["Gender"] == "Female")]

Count_of_Orders_Given_By_Male_Customers = Orders_Given_By_Male_Customers.shape[0]
Count_of_Orders_Given_By_Female_Customers = Orders_Given_By_Female_Customers.shape[0]

Ratio_of_Count_of_Orders_Given_By_Males = (Count_of_Orders_Given_By_Male_Customers / Dataset.shape[0]) * 100
Ratio_of_Count_of_Orders_Given_By_Females = (Count_of_Orders_Given_By_Female_Customers / Dataset.shape[0]) * 100

print(f"Answer - 6)\nThe Ratio Of The Number of Orders Placed By Males and Females are :-\nMales - {Ratio_of_Count_of_Orders_Given_By_Males} %\nFemales - {Ratio_of_Count_of_Orders_Given_By_Females} %")

# Question - 7: What is the ratio of the total cost of the orders placed by male and female?
Total_Cost_of_Orders_Given_By_Males = Orders_Given_By_Male_Customers["Total_Cost"].sum()
Total_Cost_of_Orders_Given_By_Females = Orders_Given_By_Female_Customers["Total_Cost"].sum()

Ratio_of_Total_Cost_of_Orders_Given_By_Males = (Total_Cost_of_Orders_Given_By_Males / Dataset["Total_Cost"].sum()) * 100
Ratio_of_Total_Cost_of_Orders_Given_By_Females = (Total_Cost_of_Orders_Given_By_Females / Dataset["Total_Cost"].sum()) * 100

print(f"Answer - 7)\nThe Ratio Of The Total Cost of Orders Placed By Males and Females are :-\nMales - {Ratio_of_Total_Cost_of_Orders_Given_By_Males} %\nFemales - {Ratio_of_Total_Cost_of_Orders_Given_By_Females} %")

# Question - 8: How many orders are placed under each order category for the country "INDIA"?
Orders_Placed_In_India = Dataset[Dataset["Country"] == "India"]["Order_Category"].value_counts()
print(f"Answer - 8)\nCategory Wise Number of Order Placed :-\n{Orders_Placed_In_India}")

# Question - 9: What is the total cost of the order placed by the customer "Willis Brinks"?
Order_Placed_By_Willis_Brinks = Dataset[Dataset["Full_Name"] == "Willis Brinks"]

Total_Cost_of_Orders_by_Willis_Brinks = Order_Placed_By_Willis_Brinks["Total_Cost"].sum()
print(f"Answer - 9)\nThe Total Cost Of Orders Placed By Willis Brinks Is $ {Total_Cost_of_Orders_by_Willis_Brinks}")

# Question - 10: Name the customer who has placed the order with the highest amount.
Name_of_Highest_Amount_Order = Dataset.loc[Dataset["Total_Cost"].idxmax(), "Full_Name"]
Order_Value = Dataset.loc[Dataset["Total_Cost"].idxmax(), "Total_Cost"]
print(f"Answer - 10)\n{Name_of_Highest_Amount_Order} Has Placed The Order With The Highest Amount Which Is $ {Order_Value}.")

# Question - 11: What is the most common order quantity?
Most_Common_Order_Quantity = Dataset["Quantity"].mode()[0]
print(f"Answer - 11)\n{Most_Common_Order_Quantity} Is the Most Common Order Frequency.")

# Question - 12: Are there specific quarters with higher order volumes?
Quater_Wise_Order = Dataset["Quater"].value_counts()
print(f"Answer - 12)\nQuarter Wise Order Volumes :-\n{Quater_Wise_Order}")

# Question - 13: How does order frequency vary over the month?
Month_Wise_Order = Dataset["Month"].value_counts()
print(f"Answer - 13)\nMonth Wise Order Frequency :-\n{Month_Wise_Order}")

# Question - 14: Are there certain categories contributing more to revenue?
Total_Revenue = Dataset["Total_Cost"].sum()
Total_Revenue_From_Small_Category = (Dataset[(Dataset["Order_Category"] == "Small Order")]["Total_Cost"].sum() / Total_Revenue) * 100
Total_Revenue_From_Normal_Category = (Dataset[(Dataset["Order_Category"] == "Normal Order")]["Total_Cost"].sum() / Total_Revenue) * 100
Total_Revenue_From_Large_Category = (Dataset[(Dataset["Order_Category"] == "Large Order")]["Total_Cost"].sum() / Total_Revenue) * 100

print(f"Answer - 14)\nCategory Wise Contribution :-\nSmall Category :- {Total_Revenue_From_Small_Category} %\nNormal Category :- {Total_Revenue_From_Normal_Category} %\nLarge Category :- {Total_Revenue_From_Large_Category}%")

# Question - 15: What is the distribution of orders across different order categories?
Cateory_Wise_Distribution = Dataset["Order_Category"].value_counts()
print(f"Answer - 15)\nCategory Wise Distribution :-\n{Cateory_Wise_Distribution}")

# Question - 16: Can you identify the most common product purchased in large orders?
Order_With_Large_Category = Dataset[(Dataset["Order_Category"] == "Large Order")]
Product_Distribution_In_Large_Orders = Order_With_Large_Category["Product_#"].value_counts()
print(f"Answer - 16)\nProduct Distribution In Karge Orders :-\n{Product_Distribution_In_Large_Orders}")

# Question - 17: What is the average quantity of products per order?
Average_Quantity = Dataset["Quantity"].mean()
print(f"Answer - 17)\nThe Average Quantity of Product Is {Average_Quantity}")

# Question - 18: Which product has the highest unit price?
Product_With_Highest_Unit_Price = Dataset.loc[Dataset["Unit_Price"].idxmax(), "Product_#"]
print(f"Answer - 18)\n{Product_With_Highest_Unit_Price} Has the Highest Unit Price.")

# Question - 19: What is the total revenue generated from large orders versus normal orders?
Total_Revenue_From_Normal_Category = (Dataset[(Dataset["Order_Category"] == "Normal Order")]["Total_Cost"].sum() / Total_Revenue) * 100
Total_Revenue_From_Large_Category = (Dataset[(Dataset["Order_Category"] == "Large Order")]["Total_Cost"].sum() / Total_Revenue) * 100

print(f"Answer - 19)\nThe Large Category Has Generated {Total_Revenue_From_Large_Category} % and Normal Category Has Generated {Total_Revenue_From_Normal_Category} % of Total Revenue")

# Question - 20: What is the proportion of large orders to normal orders in the dataset?
Order_With_Large_Category = Dataset[(Dataset["Order_Category"] == "Large Order")]
Order_With_Normal_Category = Dataset[(Dataset["Order_Category"] == "Normal Order")]
print(f"Answer - 20)\nThe Proportion of Large Order Is {(Order_With_Large_Category.shape[0] / Dataset.shape[0]) * 100} % and Normal Order Is {(Order_With_Normal_Category.shape[0] / Dataset.shape[0]) * 100} %")

# Question - 21: How many unique customers are represented in the dataset?
Unique_Customers = list(set(Dataset["Full_Name"]))
No_of_Unique_Customers = len(Unique_Customers)
print(f"Answer - 21)\nThere are {No_of_Unique_Customers} Unique Customers in the Dataset")

# Question - 22: What is the most frequently purchased product across all orders?
Frequently_Purchased_Product = Dataset["Product_#"].mode()[0]
print(f"Answer - 22)\n{Frequently_Purchased_Product} Is The Most Frequently Purchased Product")

# Question - 23: What is the average total cost for each order category?
Order_With_Large_Category = Dataset[(Dataset["Order_Category"] == "Large Order")]
Order_With_Normal_Category = Dataset[(Dataset["Order_Category"] == "Normal Order")]
Order_With_Small_Category = Dataset[(Dataset["Order_Category"] == "Small Order")]

Average_Total_Cost_In_Large_Order = Order_With_Large_Category["Total_Cost"].mean()
Average_Total_Cost_In_Normal_Order = Order_With_Normal_Category["Total_Cost"].mean()
Average_Total_Cost_In_Small_Order = Order_With_Small_Category["Total_Cost"].mean()

print(f"Answer - 23)\nCategory Wise Average Total Cost :-\nSmall Category = {Average_Total_Cost_In_Small_Order}\nNormal Cateogory = {Average_Total_Cost_In_Normal_Order}\nLarge Category = {Average_Total_Cost_In_Large_Order}")

# Question - 24: How does the quantity of products impact the total cost in different order categories?
# plt.figure(figsize=(16, 8))
# sns.barplot(x=Dataset["Quantity"], y=Dataset["Total_Cost"], hue=Dataset["Order_Category"])
# plt.show()

# Question - 25: What is the proportion of small, normal, and large orders in the dataset?
Order_With_Large_Category = Dataset[(Dataset["Order_Category"] == "Large Order")]
Order_With_Normal_Category = Dataset[(Dataset["Order_Category"] == "Normal Order")]
Order_With_Small_Category = Dataset[(Dataset["Order_Category"] == "Small Order")]
Orders_In_Large_Order = (Order_With_Large_Category.shape[0] / Dataset.shape[0]) * 100
Orders_In_Normal_Order = (Order_With_Normal_Category.shape[0] / Dataset.shape[0]) * 100
Orders_In_Small_Order = (Order_With_Small_Category.shape[0] / Dataset.shape[0]) * 100
print(f"Answer - 25)\nCategory Wise Proportion of Orders\nLarge Category :- {Orders_In_Large_Order} %\nNormal Category :- {Orders_In_Normal_Order} %\nSmall Category :- {Orders_In_Small_Order} %")
