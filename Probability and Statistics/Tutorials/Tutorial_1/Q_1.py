import pandas as pd

Dataset = pd.read_excel("./T1LA Dataset - 1.xlsx")
Dataset["Total"] = (
    Dataset["Fresh"]
    + Dataset["Milk"]
    + Dataset["Grocery"]
    + Dataset["Frozen"]
    + Dataset["Detergents_Paper"]
    + Dataset["Delicassen"]
)

# Q_1_Dataset_Channel = Dataset.groupby("Channel")["Total"].mean()
# Q_1_Dataset_Region = Dataset.groupby("Region")["Total"].mean()
# print(f"Channel Wise Spendings :- \n{Q_1_Dataset_Channel}")
# print(f"Region Wise Spendings :- \n{Q_1_Dataset_Region}")

# Items = ["Fresh", "Milk", "Grocery", "Frozen", "Detergents_Paper", "Delicassen"]
# Standatd_Deviation = []

# for item in Items :
#     Standatd_Deviation.append(Dataset[item].std())

# Q_3_Answer = pd.DataFrame()
# Q_3_Answer["Items"] = Items
# Q_3_Answer["Standatd Deviation"] = Standatd_Deviation

# print("Product Wise Standard Deviation :- ")
# print(Q_3_Answer.to_string(index=False))


def detect_outliers_iqr(data):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = data[(data < lower_bound) | (data > upper_bound)]
    return list(outliers)


Items = ["Fresh", "Milk", "Grocery", "Frozen", "Detergents_Paper", "Delicassen"]
outliers_list = []

for item in Items:
    outliers_list.append(detect_outliers_iqr(Dataset[item]))

Q_4_Answer = pd.DataFrame({"Items": Items, "Outliers": outliers_list})

print(Q_4_Answer.to_string(index = False))
