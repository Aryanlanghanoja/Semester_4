import random

import pandas as pd


def Generate_Numbers() :
    Numbers = []

    while True :
        Choice = int(input("Enter Your Choice Your Generating Data :-\n1)Integer\n2)Fraction with One Deciaml\n3)Fraction with Two Decimal\n"))
        if(Choice in [1,2,3]) :
            break
        else :
            print("Enter A Valid Choice")

    while True:
        Lower_Limit = int(input("Enter The Lower Limit :-"))
        Upper_Limit = int(input("Enter The Upper Limit :- "))

        if(Upper_Limit > Lower_Limit) :
            break;

        else :
            print("Upper Limit Should Be Greater Than Lower Limit :-")

    if(Choice == 1) :
        for i in range(0,12) :
            Numbers.append(random.randint(Lower_Limit,Upper_Limit))

    elif (Choice == 2) :
        for i in range(0,12) :
            Numbers.append(round(random.uniform(Lower_Limit,Upper_Limit),1))

    else :
        for i in range(0, 12):
            Numbers.append(round(random.uniform(Lower_Limit, Upper_Limit), 2))
            
    return Numbers


def Calculate_Mean(Data) :
    return sum(Data) / len(Data) 


def Calculate_Median(Input_Data):
    Data = sorted(Input_Data)
    if len(Data) % 2 == 0:
        return (Data[len(Data) // 2] + Data[len(Data) // 2 - 1]) / 2
    else:
        return Data[(len(Data) // 2)]

def Calculate_Mode(Data) :
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
    ).reset_index(drop=True)

    Mode = [
        Frequency_Distribution["Observation"][i]
        for i in range(len(Frequency_Distribution["Observation"]))
        if Frequency_Distribution["Frequency"][i]
        == Frequency_Distribution["Frequency"].iloc[0]
    ]
    
    return Mode 

def Print_Result(Data , Mean ,Median, Mode) :
    print(f"Statistical Value for {Data}")
    print("Mean: ", Mean)
    print("Median:", Median)
    print("Mode: ", Mode)
    

Data = []
Data = Generate_Numbers()
Mean = Calculate_Mean(Data)
Median = Calculate_Median(Data)
Mode = Calculate_Mode(Data)
Print_Result(Data , Mean , Median , Mode)


