import pandas as pd
import plotly.express as px

Dataset_Sales_and_Numbers = pd.read_excel(
    "./Dataset.xlsx", "Sales"
) 
Dataset_Nubers_and_Months = pd.read_excel(
    "./Dataset.xlsx", "Name"
)  

Merged_Dataset = pd.merge(
    Dataset_Sales_and_Numbers, Dataset_Sales_and_Numbers, on="Number"
)
Final_Dataset = Merged_Dataset[["Month", "Sales"]]
Final_Dataset = Final_Dataset.groupby("Month").sum().reset_index()
Final_Dataset = Final_Dataset.sort_values(by="Sales", ascending=False)

Final_Dataset["Sales_Label"] = Final_Dataset["Sales"].astype(str)

Figure = px.bar(
   Final_Dataset,
    x="Month",
    y="Sales",
    color="Month",
    title="Sales by Month",
    labels={"Sales": "Total Sales", "Month": "Month Name"},
    text="Sales_Label",
)

Figure.update_traces(textposition="outside")
Figure.write_html("sales_by_month_plot.html")
