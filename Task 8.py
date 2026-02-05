import pandas as pd

df = pd.read_csv("students.csv")

subjects = ["Subject1", "Subject2", "Subject3", "Subject4", "Subject5"]

df["Average"] = df[subjects].mean(axis=1)

print("Таблиця студентів із середнім балом:")
print(df[["Name", "Surname", "Average"]])

group_average = df[subjects].mean()

print("\nСередній бал групи з дисциплін:")
print(group_average)