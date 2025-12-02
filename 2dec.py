import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

df = pd.read_csv("vgsales.csv")

# plt.hist(df["Genre"],bins=8)
# plt.hist(df["Year"],bins=4)

"""sns.histplot(df["Year"],bins=8)
plt.xticks(rotation=90)
plt.show()

"""

a=np.array([-5,-2,3,-5,5,4,4,7,9,20,10,2,1,0,45])
# sns.boxplot(a)
# plt.show()

# df_temp = df.drop(columns=["Year","Rank"])
# sns.boxplot(data=df_temp)
"""plt.show()

sns.boxplot(data=df["Global_Sales"])
plt.show()

"""

# a= df["Name"].value_counts()
# print(a)


#Sales of Ice Hockey in NA region (NA_Sales) 

ih= df.loc[df['Name']=="Ice Hockey"]
# print(ih)


sns.lineplot(data=ih,x="Year",y="NA_Sales")
plt.title("Ice Hockey Sales in NA")
plt.ylabel("Sales")
plt.grid(True)
plt.show()
