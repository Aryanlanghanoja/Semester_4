import pandas as pd


def Calculate_Frequency_Distribution(Data):
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

    return Frequency_Distribution


Input = input("Enter space-separated values: ")
Data = [float(i) for i in Input.split()]

Frequency_Distribution = Calculate_Frequency_Distribution(Data)
Mean = sum(Data) / len(Data)
Median = 0
Mode = [
    Frequency_Distribution["Observation"][i]
    for i in range(len(Frequency_Distribution["Observation"]))
    if Frequency_Distribution["Frequency"][i]
    == Frequency_Distribution["Frequency"].iloc[0]
]

if len(Data) % 2 == 0:
    Median = (Data[len(Data) // 2] + Data[len(Data) // 2 - 1]) / 2
else:
    Median = Data[len(Data) // 2]

if Median < Mean:
    Shape = "Right Skewed"
elif Median > Mean:
    Shape = "Left Skewed"
else:
    Shape = "Normal Distribution"

if len(Mode) == 1:
    Distribution = "Unimodal"
elif len(Mode) == 2:
    Distribution = "Bimodal"
else:
    Distribution = "Multimodal"

print("Frequency Distribution:")
print(Frequency_Distribution.to_string(index=False))
print()
print("Mean:", Mean)
print("Median:", Median)
print("Mode:", Mode)
print("Distribution:", Distribution)
print("Shape:", Shape)
