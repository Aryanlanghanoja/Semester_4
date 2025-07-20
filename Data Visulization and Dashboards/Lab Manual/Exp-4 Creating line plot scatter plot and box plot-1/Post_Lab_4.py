# Importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Reading the dataset from an Excel file
Dataset = pd.read_excel("D:/Aryan Data/Usefull Data/Semester - 4/Data Visulization and Dashboards/Lab Manual/Exp-4 Creating line plot scatter plot and box plot-1/Sample - Superstore.xlsx", "Orders")

# Line Chart for State vs Quantity
Quantity_State_Grouped_Dataset = Dataset.groupby(by="State")["Quantity"].sum()

# Plotting the line chart
Quantity_State_Grouped_Dataset.plot(kind="line", color="b")
plt.title("Line Chart of State Vs Quantity")
plt.xlabel("State")
plt.ylabel("Quantity")
plt.show()

# Line Chart for State vs Profit
Profit_State_Grouped_Dataset = Dataset.groupby(by="State")["Profit"].sum()

# Plotting the line chart
Profit_State_Grouped_Dataset.plot(kind="line", color="b")
plt.title("Line Chart of State Vs Profit")  # Fix the title to represent Profit
plt.xlabel("State")
plt.ylabel("Total Profit")
plt.show()

# Scatter Plot for Quantity vs Total Profit
Total_Sale_Grouped_Total_Sale = Dataset.groupby(by="Quantity")["Profit"].sum()
Total_Sale_Grouped_Total_Sale = Total_Sale_Grouped_Total_Sale.reset_index()

# Plotting the scatter plot
plt.scatter(
    Total_Sale_Grouped_Total_Sale["Quantity"],
    Total_Sale_Grouped_Total_Sale["Profit"],
    c="g",
    marker="o",
)
plt.title("Scatter Plot for Total Profit Vs Quantity")
plt.xlabel("Quantity")
plt.ylabel("Total Profit")
plt.show()

# Box Plot using Matplotlib
Parameters_of_Box_Plots = ["Sales", "Quantity", "Discount", "Profit"]

# Creating a box plot for selected parameters
plt.figure(figsize=(12, 8))
plt.boxplot(
    [Dataset[column] for column in Parameters_of_Box_Plots],
    labels=Parameters_of_Box_Plots,
)
plt.title("Box Plot for Sales, Quantity, Discount, and Profit")
plt.xlabel("Columns")
plt.ylabel("Values")
plt.show()
