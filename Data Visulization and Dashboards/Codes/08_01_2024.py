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


# Que - 4 :- 

# mod means the Value which has the highest frequency
Dataset['Order_Date'] = pd.to_datetime(Dataset['Order_Date'])
Dataset['Month_Python'] = Dataset['Order_Date'].dt.month
Highest_Month = Dataset['Month_Python'].mode()[0]


# Que - 5 :- 

Dataset['Year_Python'] = Dataset['Order_Date'].dt.year
Year_wise_average_cost = Dataset.groupby('Year_Python')['Total_Cost'].mean()
Year_wise_average_cost.idxmax()

# Que - 6 :- 

Genderwise_order = Dataset.groupby('Gender')['Order_#'].count()
Ratio_of_Males = Genderwise_order[1] / Dataset['Order_#'].count()
Ratio_of_Females = Genderwise_order[0] / Dataset['Order_#'].count()


# Que - 7 :-

Genderwise_total_cost = Dataset.groupby('Gender')['Total_Cost'].sum()
Ratio_of_total_Cost_Males = Genderwise_total_cost[1] / Dataset['Total_Cost'].sum()
Ratio_of_total_Cost_Females = Genderwise_total_cost[1] / Dataset['Total_Cost'].sum()


# Que - 8 :- 
 
Small_Orders_India = Dataset[(Dataset['Country'] == "India") & (Dataset['Order_Category'] == "Small Order")].count()
Normal_Orders_India = Dataset[(Dataset['Country'] == "India") & (Dataset['Order_Category'] == "Normal Order")].count()
Large_Orders_India = Dataset[(Dataset['Country'] == "India") & (Dataset['Order_Category'] == "Large Order")].count()

India_Count = Dataset[Dataset['Country'] == "India"]['Order_Category'].value_counts()


# Que - 9 




# Que - 10 

Name = Dataset.loc[Dataset['Total_Cost'].idxmax() , 'Name']