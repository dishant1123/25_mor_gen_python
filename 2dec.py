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


"""
sns.lineplot(data=ih,x="Year",y="NA_Sales")
plt.title("Ice Hockey Sales in NA")
plt.ylabel("Sales")
plt.grid(True)
plt.show()
"""

# sales of NEED FOR SPEED in NA region (NA_Sales)

# sales trend  in ICE HOCKEY in north amrecia region   ===>  trnd  line  ==> line plot 

# top  3 publisher ,top3 genres , top 3 platforms

nfs =df.loc[(df['Name'].str.contains("Need For Speed"))| (df['Name'].str.contains("Need For Speed"))]

# print(nfs)

# sns.lineplot(data=nfs,x=nfs["Year"],y=nfs["Global_Sales"])
# plt.title("Need For Speed Sales in NA")
# plt.ylabel("Sales")
# plt.grid(True)
# plt.show()

"""base_ball =df.loc[df['Name']=="Baseball"]
print(base_ball)

sns.lineplot(data=base_ball,x=base_ball["Year"],y=base_ball["NA_Sales"],label="Baseball",color="red",marker="o")
sns.lineplot(data=ih,x="Year",y="NA_Sales",label="Ice Hockey",color="blue",marker="o")
plt.title("comparison between ice hockey and baseball sales in north america")
plt.ylabel("Sales")
plt.xlabel("Year")
plt.grid(True)
# plt.legend(loc="upper left")
plt.show()
"""

top3_publishers = df["Publisher"].value_counts().index[:3]
top3_genres = df["Genre"].value_counts().index[:3]
top3_platforms = df["Platform"].value_counts().index[:3]
top3_data = df.loc[df["Publisher"].isin(top3_publishers) & df["Genre"].isin(top3_genres) & df["Platform"].isin(top3_platforms)]
# print(top3_data)

# sns.jointplot(data=top3_data, x="NA_Sales", y="JP_Sales")

# sns.scatterplot(data=top3_data, x="NA_Sales", y="JP_Sales",hue="Genre",size="Global_Sales",sizes=(1,100))

sns.boxplot(data=top3_data, x="Publisher", y="Global_Sales",hue="Genre")
plt.show()