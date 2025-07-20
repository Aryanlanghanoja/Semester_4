import math

import pandas as pd

Dataset = pd.read_excel("./T1LA Dataset - 3.xlsx")
print(Dataset.columns)


def Calculate_Median(Data):
    if len(Data) % 2 == 0:
        return (Data[len(Data) // 2] + Data[len(Data) // 2 - 1]) / 2
    else:
        return Data[len(Data) // 2]


def Calculate_SD(data):
    mean = sum(data) / len(data)
    Sigma_Xi_x = sum((i - mean) ** 2 for i in data)
    Sigma_Xi_x = Sigma_Xi_x / (len(data) - 1)
    Standard_Deviation = math.sqrt(Sigma_Xi_x)
    return Standard_Deviation


def Descriptive_Statistics(Data):
    Frequency_Distribution = {}

    for i in Data:
        if i in Frequency_Distribution:
            Frequency_Distribution[i] += 1
        else:
            Frequency_Distribution[i] = 1

    Frequency_Distribution = pd.DataFrame(
        list(Frequency_Distribution.items()), columns=["Observation", "Frequency"]
    )

    Frequency_Distribution = Frequency_Distribution.sort_values(
        by="Frequency", ascending=False
    ).reset_index()

    Mean = sum(Data) / len(Data)
    Median = Calculate_Median(Data)
    Q1 = Calculate_Median(Data[: len(Data) // 2])
    Q2 = Calculate_Median(Data)
    Q3 = Calculate_Median(Data[len(Data) // 2 :])
    Minimum = min(Data)
    Maximum = max(Data)
    IQR = Q3 - Q1
    Lower_Limit = Q1 - (1.5 * IQR)
    Upper_Limit = Q3 + (1.5 * IQR)
    Range = Maximum - Minimum
    No_of_Observation = len(Data)
    Standard_Deviation = Calculate_SD(Data)
    Variance = Standard_Deviation**2
    Mode = [
        Frequency_Distribution["Observation"][i]
        for i in range(len(Frequency_Distribution["Observation"]))
        if Frequency_Distribution["Frequency"][i]
        == Frequency_Distribution["Frequency"].iloc[0]
    ]

    print("Description of Crediti Card Usage")
    print("Mean: ", Mean)
    print("Median:", Median)
    print("Mode:", Mode)
    print("Q1:", Q1)
    print("Q2:", Q2)
    print("Q3:", Q3)
    print("Minimum:", Minimum)
    print("Maximum:", Maximum)
    print("IQR:", IQR)
    print("Lower Limit:", Lower_Limit)
    print("Upper Limit:", Upper_Limit)
    print("Range:", Range)
    print("No. of Observations:", No_of_Observation)
    print("Standard Deviation:", Standard_Deviation)
    print("Variance:", Variance)

Data = sorted(list(Dataset["Amount"]))
Descriptive_Statistics(Data)

Male = Dataset[Dataset["Gender"] == "M"]
Female = Dataset[Dataset["Gender"] == "F"]

if (
    (Male["Amount"].mean() <= 1.2 * Female["Amount"].mean())
    and (Male["Amount"].mean() >= 0.8 * Female["Amount"].mean())
) or (
    (Female["Amount"].mean() <= 1.2 * Male["Amount"].mean())
    and (Female["Amount"].mean() >= 0.8 * Male["Amount"].mean())
):
    print("The Average Uses are not Varies with Sex")
else:
    print("The Average Uses are Varies with Sex")

print(set(Dataset["Exp Type"]))


Do_Shopping = Dataset[
    (Dataset["Exp Type"] == "Grocery") | (Dataset["Exp Type"] == "Food")
]

Dont_Do_Shopping = Dataset[
    (Dataset["Exp Type"] != "Grocery") | (Dataset["Exp Type"] != "Food")
]

if (
    (Do_Shopping["Amount"].mean() <= 1.2 * Dont_Do_Shopping["Amount"].mean())
    and (Do_Shopping["Amount"].mean() >= 0.8 * Dont_Do_Shopping["Amount"].mean())
) or (
    (Dont_Do_Shopping["Amount"].mean() <= 1.2 * Do_Shopping["Amount"].mean())
    and (Dont_Do_Shopping["Amount"].mean() >= 0.8 * Do_Shopping["Amount"].mean())
):
    print("The Average Uses are not Varying")
else:
    print("The Average Uses are Varying")

Do_Banking = Dataset[(Dataset["Exp Type"] == "Bills")]
Dont_Do_Banking = Dataset[(Dataset["Exp Type"] != "Bills")]

if (
    (Do_Banking["Amount"].mean() <= 1.2 * Dont_Do_Banking["Amount"].mean())
    and (Do_Banking["Amount"].mean() >= 0.8 * Dont_Do_Banking["Amount"].mean())
) or (
    (Dont_Do_Banking["Amount"].mean() <= 1.2 * Do_Banking["Amount"].mean())
    and (Dont_Do_Banking["Amount"].mean() >= 0.8 * Do_Banking["Amount"].mean())
):
    print("The Average Uses are not Varying")
else:
    print("The Average Uses are Varying")

Shopping_And_Gender = Dataset[(Dataset["Exp Type"] == "Grocery") | (Dataset["Exp Type"] == "Food")]
Aggregate_Average_for_Gender_and_Shopping = Shopping_And_Gender.groupby(["Gender", "Exp Type"])['Amount'].mean()
print(Aggregate_Average_for_Gender_and_Shopping)

Shopping_And_Gender_And_Banking = Dataset[
    (Dataset["Exp Type"] == "Grocery")
    | (Dataset["Exp Type"] == "Food")
    | (Dataset["Exp Type"] == "Bills")
]
Aggregate_Average_for_Gender_and_Shopping_and_Banking = (
    Shopping_And_Gender_And_Banking.groupby(["Gender", "Exp Type"])["Amount"].mean()
)
print(Aggregate_Average_for_Gender_and_Shopping_and_Banking)
