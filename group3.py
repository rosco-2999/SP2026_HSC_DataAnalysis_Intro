# Create a program that tells how many of each passenger was in each P class and how many survived and did not survive in each P class.
# Show the results on a chart.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Titanic-Dataset.csv")


total_per_class = df.groupby("Pclass").size()
print("Total passengers per class:")


survivors_per_class = df[df["Survived"] == 1].groupby("Pclass").size()
print("\nSurvivors per class:")


summary = df.groupby("Pclass").agg(
    Total_Passengers=("Survived", "count"),
    Survived=("Survived", "sum")
)



counts = df.groupby(["Pclass", "Survived"]).size().unstack() 

counts.plot(kind="bar")

plt.title("Titanic Survival by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")
plt.legend(["Did Not Survive", "Survived"])

plt.tight_layout()
plt.show()
plt.savefig("output.png")