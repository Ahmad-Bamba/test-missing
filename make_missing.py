import pandas as pd
import numpy as np
import random
import copy

df_orig = pd.read_csv('data/test_data.csv')
df = copy.copy(df_orig)


df.loc[df.sample(frac=0.1).index, 'tiv_2011'] = np.nan
df.loc[df.sample(frac=0.1).index, 'tiv_2012'] = np.nan

df.to_csv('data/blind_missing.csv')

del df
df = copy.copy(df_orig)

for index, row in df.iterrows():
    if row['race'] == 'black':
        x = random.randint(1, 100)
        if x <= 90:
            df.loc[index, 'tiv_2011'] = np.nan
        y = random.randint(1, 100)
        if y <= 90:
            df.loc[index, 'tiv_2012'] = np.nan

df.to_csv('data/biased_missing.csv')
