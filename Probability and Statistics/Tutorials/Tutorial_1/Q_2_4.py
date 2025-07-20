import math


def Calculate_SD(data_unsorted) :
    data = sorted(data_unsorted)
    mean = 0 

    for i in data :
        mean = mean + i

    mean = mean / len(data)

    Sigma_Xi_x = 0 

    for i in data :
        Sigma_Xi_x = Sigma_Xi_x + (i - mean) ** 2

    Sigma_Xi_x = Sigma_Xi_x / (len(data) - 1)

    Standard_Deviation = math.sqrt(Sigma_Xi_x)

    return Standard_Deviation


Input = input("Enter A Space Seprated Value :-")
Data = []

for i in Input.split(" "):
    Data.append(float(i))


Standard_Deviation = Calculate_SD(Data)
Variance = Standard_Deviation ** 2

print(f"For Data :- {Data} :- Standard Deviation = {Standard_Deviation}\nVariance = {Variance}")