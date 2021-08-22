import pandas as pd
import numpy as np
import matplotlib.pyplot as plt                                                                           
import seaborn as sns

df = pd.read_csv("wc.csv")

"""This shows the structure of the data."""

df.head(5)

df.info

df = df[['names', 'timestamp', 'hours', 'days', 'months']]
df.head()

df['names'].unique()

df.head()

"""The graph below shoes the number hours spent in chating."""

sns.countplot(x="names", data=df, palette="viridis")

"""the graphs below shows the number of times a person chated in a given time. """

plt.figure(figsize = (15,5))
sns.countplot(x="hours", data=df[df["names"] == "Person1"], palette="viridis")

plt.figure(figsize = (15,5))
sns.countplot(x="hours", data=df[df["names"] == "Person2"], palette="viridis")



plt.figure(figsize = (15,5))
sns.countplot(x="hours", data=df[df["names"] == "Person3"], palette="viridis")



plt.figure(figsize = (15,5))
sns.countplot(x="hours", data=df[df["names"] == "Person4"], palette="viridis")

plt.figure(figsize = (15,5))
sns.countplot(x="months", data=df, hue="names", palette="viridis")

plt.figure(figsize = (15,5))
sns.countplot(x="hours", data=df, hue="names", palette="viridis")

"""The graph shows the comparison between all the persons chating on the whatsapp.

"""
