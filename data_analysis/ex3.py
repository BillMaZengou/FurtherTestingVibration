import glob
from os import path
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('whitegrid')

def add_transparency(ax):
    for patch in ax.artists:
     r, g, b, a = patch.get_facecolor()
     patch.set_facecolor((r, g, b, .8))

distance = 0.7151338
width = 0.87
ID = np.log2(2*distance/width)

drop = dict()
reaction_time = dict()
for file in glob.glob("../result/Ex3/*/*/*"):
    mode = file.split('/')[-2]
    record = file.split('/')[-1]
    if mode not in drop:
        drop[mode] = []
        reaction_time[mode] = []

    with open(file, 'r') as f:
        read_data = f.readlines()
    for i in read_data[1:]:
        i = i.split(",")[-2].split(" ")[1]
        if i != "Null":
            i = float(i)
            reaction_time[mode].append(i)
        else:
            reaction_time[mode].append(np.nan)

    drop_num = int(read_data[0].split(':')[-1])
    drop_rate = drop_num/15
    drop[mode].append(drop_rate)

df1 = pd.DataFrame(drop)
df2 = pd.DataFrame(reaction_time)
cols = ['vision_only', 'sym_vib', 'vib_only', 'random_vib']
df1 = df1[cols]
df2 = df2[cols]
names = ["No\nVibration", "Symmetric\nVibration", "Asymmetric\nVibration", "Randomized\nAsymmetric\nVibration"]
df1.columns = names
df2.columns = names
sns.set(font_scale=0.9)

ax1 = sns.boxplot(data=df1, width=0.5, showmeans=True, palette="Reds")
ax1.set(xlabel='Different Vibration Modes', ylabel='Drop Rate')
ax1.set_title("Drop Rate For Different Vibration Modes With The Same ID")
add_transparency(ax1)
plt.show()

ax2 = sns.boxplot(data=df2, width=0.5, showmeans=True, palette="Reds")
ax2.set(xlabel='Different Vibration Modes', ylabel='Operation Time')
ax2.set_title("MT For Different Vibration Modes With The Same ID")
add_transparency(ax2)
plt.show()

"""Statistical Test"""

names = ["No_Vibration", "Symmetric_Vibration", "Asymmetric_Vibration", "Randomized_Asymmetric_Vibration"]
df1.columns = names
df2.columns = names

import scipy.stats as stats
# stats f_oneway functions takes the groups as input and returns F and P-value
# fvalue, pvalue = stats.f_oneway(df1["No_Vibration"], df1["Symmetric_Vibration"], df1["Asymmetric_Vibration"], df1["Randomized_Asymmetric_Vibration"])
fvalue, pvalue = stats.f_oneway(df2["No_Vibration"], df2["Symmetric_Vibration"], df2["Asymmetric_Vibration"], df2["Randomized_Asymmetric_Vibration"])
print(fvalue, pvalue)

# get ANOVA table as R like output
import statsmodels.api as sm
from statsmodels.formula.api import ols
# reshape the d dataframe suitable for statsmodels package
# d_melt = pd.melt(df1.reset_index(), id_vars=['index'], value_vars=names)
d_melt = pd.melt(df2.reset_index(), id_vars=['index'], value_vars=names)
# replace column names
d_melt.columns = ['index', 'Vibration_Modes', 'value']
# Ordinary Least Squares (OLS) model
model = ols('value ~ C(Vibration_Modes)', data=d_melt).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)

from pingouin import pairwise_tukey
m_comp = pairwise_tukey(data=d_melt, dv='value', between='Vibration_Modes')
print(m_comp)

w, pvalue = stats.shapiro(model.resid)
print(w, pvalue)
