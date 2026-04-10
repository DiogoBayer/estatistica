#%%

import pandas as pd

df = pd.read_csv("data/points_tmw.csv")
df

#%%

df.groupby(["descProduto"])[["idTransacao"]].count()