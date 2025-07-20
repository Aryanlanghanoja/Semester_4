import math


def Calculate_Population_Mean(Data):
    Population_Mean = sum(Data) / len(Data)
    return Population_Mean


def Calculate_Population_SD(Data):
    Mean = Calculate_Population_Mean(Data)

    Sum = 0
    for observation in Data:
        Sum += observation * observation

    Population_SD = math.sqrt((Sum / len(Data)) - (Mean**2))

    return Population_SD


def Calculate_Z_Score(Data):
    Population_Mean = Calculate_Population_Mean(Data)
    Population_SD = Calculate_Population_SD(Data)

    Z_Scores = []

    for Observation in Data:
        Z_Scores.append((Observation - Population_Mean) / Population_SD)

    return Z_Scores


Input = input("Enter A Space Seprated Value :-")
Data = []

for i in Input.split(" "):
    Data.append(float(i))

Z_Scores = Calculate_Z_Score(Data)

print(f"The Z-Scores for {Data} is :-\n{Z_Scores}")
