import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')

print(df.head())
print(df.info())
print(df.isnull().sum())

sns.barplot(x='sex', y='survived', data=df)
plt.title("Survival by Gender")
plt.show()

sns.barplot(x='pclass', y='survived', data=df)
plt.title("Survival by Class")
plt.show()

df['age_group'] = pd.cut(df['age'], bins=[0,12,18,35,60,100],
                        labels=['Child','Teen','Young','Adult','Senior'])

sns.barplot(x='age_group', y='survived', data=df)
plt.title("Survival by Age Group")
plt.show()
