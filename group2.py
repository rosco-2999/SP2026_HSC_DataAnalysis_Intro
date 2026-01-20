# Create a program that creates age categories. Then create a plot or chart that shows how many individuals of each age group survived and did not survive.

import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np

df = pd.read_csv("Titanic-Dataset.csv")

age = df['Age']
survivors = df["Survived"]




bins1 = [0, 1]
la


bins2 = [0, 13, 18, 65, ]
labels2 = ["0-13", "13 18", "18 - 65", ">65"]

    



