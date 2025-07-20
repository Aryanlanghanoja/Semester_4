import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

Dataset = pd.read_excel("./Sample - Superstore.xlsx", "Orders")
# print(Dataset)

# print(Dataset.shape)
# print(Dataset.columns)
# print(Dataset.info())
# print(Dataset.head())
# print(Dataset.tail())
print(Dataset.isnull())
print(Dataset.isnull().sum())
print(Dataset.isnull().sum().sum())
print(Dataset.nunique())

Dataset = Dataset.drop(columns=["Postal Code"], axis=1)
print(Dataset.columns)

State_Wise_Counts = Dataset["State"].value_counts(ascending=True)
print(State_Wise_Counts)
