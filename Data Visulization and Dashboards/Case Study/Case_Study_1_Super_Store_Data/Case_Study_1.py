import bs4
import pandas as pd

Dataset = pd.read_excel("./Superstore.xlsx", "Orders")

Region_wise_sub_category_count = subcat_count_region_wise = (
    Dataset.groupby(["Region", "Sub-Category"]).size().reset_index(name="Count")
)
print(Region_wise_sub_category_count)
