import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

Dataset = pd.read_excel("./Tutorial 2 Tk1 A batch_MU_Students.xlsx", sheet_name="Q.2")

# contingency_table_1 = pd.crosstab(Dataset["Major"], Dataset["Gender"])
# print("Contingency Table for Gender and Major:")
# print(contingency_table_1)

# contingency_table_2 = pd.crosstab(Dataset["Grad Intention"], Dataset["Gender"])
# print("Contingency Table for Gender and Grand Intention:- ")
# print(contingency_table_2)

# contingency_table_3 = pd.crosstab(Dataset["Employment"], Dataset["Gender"])
# print("Contingency Table for Gender and Employment:- ")
# print(contingency_table_3)

# contingency_table_4 = pd.crosstab(Dataset["Computer"], Dataset["Gender"])
# print("Contingency Table for Gender and Computer:- ")
# print(contingency_table_4)

# print(f"The Probability that a randomly selected MU student will be male is {"{:.3f}".format((Dataset[(Dataset['Gender'] == "Male")].shape[0] / Dataset.shape[0]) * 100)} %")
# print(f"The Probability that a randomly selected MU student will be female is {"{:.3f}".format((Dataset[(Dataset['Gender'] == "Female")].shape[0] / Dataset.shape[0]) * 100)} %")

# Males_Data = Dataset[(Dataset['Gender'] == "Male")]
# print("Conditional Probability of different majors among the male students in MU :-")
# print(Males_Data["Major"].value_counts(normalize=True))

# Females_Data = Dataset[(Dataset["Gender"] == "Female")]
# print("Conditional Probability of different majors among the female students in MU :-")
# print(Females_Data["Major"].value_counts(normalize=True))

# Corrected version
# Graduate_Male = Dataset[(Dataset["Gender"] == "Male") & (Dataset["Grad Intention"] == "Yes")]

# probability = '{:.3f}' .format(Graduate_Male.shape[0] / Dataset.shape[0])
# print(f"The Probability That a randomly chosen student is a male and intends to graduate is {probability} %")

# Not_Laptop_Feale = Dataset[(Dataset["Gender"] == "Female") & (Dataset["Computer"] != "Laptop")]

# probability = "{:.3f}".format(Not_Laptop_Feale.shape[0] / Dataset.shape[0])
# print(f"The Probability That a randomly chosen student is a Female and not having laptop is {probability}")

# Male_or_full_time = Dataset[(Dataset["Gender"] == "Male") | (Dataset["Employment"] == "Full-Time")]
# probability = "{:.3f}".format(Male_or_full_time.shape[0] / Dataset.shape[0])
# print(f"The Probability that a randomly chosen student is either a male or has full-time employment is {probability}")

# Female_or_full_time = Dataset[(Dataset["Gender"] == "Female")& ((Dataset["Major"] == "Management")| (Dataset["Major"] == "International Business"))]
# probability = "{:.3f}".format(Female_or_full_time.shape[0] / Dataset.shape[0])
# print(f"The Probability that given a female student is randomly chosen, she is majoring in international business or management. is {probability}")

# subset = Dataset[Dataset["Grad Intention"].isin(["Yes", "No"])]
# cont_table = pd.crosstab(subset["Gender"], subset["Grad Intention"])
# print(cont_table)
# sum = 0

# for i in range(0,2) :
#     for j in range(0,2) :
#         sum = sum + cont_table.iloc[i, j]

# for i in range(0, 2):
#     for j in range(0, 2):
#         cont_table.iloc[i, j] = cont_table.iloc[i, j] / sum

# print(cont_table)

# p_female = 0
# graduate = 0

# for i in range(0, 2):
#     p_female = p_female + cont_table.iloc[0, i]

# for i in range(0, 2):
#     graduate = graduate + cont_table.iloc[i, 1]

# if (cont_table.iloc[0, 1] == p_female * graduate) :
#     print("The Events are Independent")

# else :
#     print("The Events are Dependent")


table = pd.crosstab(index=Dataset["Gender"],columns=pd.cut(Dataset["Wealth"], bins=[-1, 49, 100], labels=["<50", ">=50"]),)
total_males = table.loc["Male"].sum()
total_females = table.loc["Female"].sum()
prob_male_50_or_more = table.loc["Male", ">=50"] / total_males
prob_female_50_or_more = table.loc["Female", ">=50"] / total_females
print("Conditional probability that a randomly selected male earns 50 or more: {:.2%}".format(prob_male_50_or_more))
print("Conditional probability that a randomly selected female earns 50 or more: {:.2%}".format(prob_female_50_or_more))
