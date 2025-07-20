def Calculate_Median(Data) :
    if(len(Data) % 2 == 0) :
        return (Data[len(Data) // 2] + Data[len(Data) // 2 - 1]) / 2
    else : 
        return Data[(len(Data) // 2)]

def Five_Plot_Summary(Data) :
    Q2 = Calculate_Median(Data)
    Q1 = 0
    Q3  = 0 
    Lower_Quartile = []
    Upper_Quartile = []
    if(len(Data) % 2 == 0) :
        Lower_Quartile = Data[:((len(Data) // 2))]
        Upper_Quartile = Data[len(Data) // 2 :]

    else :
        Lower_Quartile = Data[:((len(Data) // 2))]
        Upper_Quartile = Data[(len(Data) // 2) + 1 :]

    Q1 = Calculate_Median(Lower_Quartile)
    Q3 = Calculate_Median(Upper_Quartile)
    
    IQR = Q3 - Q1
    Min = min(Data)
    Max= max(Data)
    Lower_Limit = Q1 - (1.5 * IQR)
    Upper_Limit = Q3 + (1.5 * IQR)    
    Outliers = []
    
    for i in Data :
        if(i < Lower_Limit or i > Upper_Limit):
            Outliers.append(i)
    
    print(f"Five Point Summary of Box Plot For {Data} :\nMinimum = {Min}\nMaximum = {Max}\nQ1 = {Q1}\nQ2 = {Q2}\nQ3 = {Q3}\nIQR = {IQR}\nLower Limit = {Lower_Limit}\nUpper Limit = {Upper_Limit}\nOutliers = {Outliers}\n")


Input = input("Enter A Space Seprated Value :-")
Data = []

for i in Input.split(" "):
    Data.append(float(i))

Data_Sorted = sorted(Data)
Five_Plot_Summary(Data_Sorted)

