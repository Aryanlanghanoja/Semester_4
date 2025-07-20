import pandas as pd
import plotly.graph_objs as go

Dataset = pd.read_excel("./T1LA Dataset - 1.xlsx")

def Calculate_Median(Data_Unsorted):
    Data = sorted(Data_Unsorted)
    if len(Data) % 2 == 0:
        return (Data[len(Data) // 2] + Data[len(Data) // 2 - 1]) / 2
    else:
        return Data[len(Data) // 2]


def Five_Plot_Summary(Data_Unsorted):
    Data = sorted(Data_Unsorted)
    Q2 = Calculate_Median(Data)
    Q1 = Calculate_Median(Data[: len(Data) // 2])
    Q3 = Calculate_Median(Data[len(Data) // 2 :])
    IQR = Q3 - Q1
    Min = min(Data)
    Max = max(Data)
    Lower_Limit = Q1 - (1.5 * IQR)
    Upper_Limit = Q3 + (1.5 * IQR)
    Outliers = [i for i in Data if i < Lower_Limit or i > Upper_Limit]

    print(
        f"Minimum = {Min}\nMaximum = {Max}\nQ1 = {Q1}\nQ2 = {Q2}\nQ3 = {Q3}\nIQR = {IQR}\nLower Limit = {Lower_Limit}\nUpper Limit = {Upper_Limit}\nOutliers = {Outliers}\n"
    )

for column in Dataset.columns:
    Data = list(Dataset[column])
    print(f"Five Point Summary of Box Plot For {column} :\n")
    Five_Plot_Summary(Data)

Traces = []

for column in Dataset.columns:
    Trace = go.Box(y=Dataset[column], name=column)
    Traces.append(Trace)

layout = go.Layout(title="Box Plot", yaxis=dict(title="Values"))
Figure = go.Figure(data=Traces, layout=layout)
Figure.write_html("Q_2_5.html")

