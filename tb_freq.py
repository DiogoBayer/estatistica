#%%

import pandas as pd

df = pd.read_csv("data/points_tmw.csv")
df

#%%

freq_produto = (df.groupby(["descProduto"])[["idTransacao"]]
                .count())

freq_produto["Freq. Abs. Acum."] = freq_produto["idTransacao"].cumsum()

freq_produto["Freq. Rel."]= freq_produto["idTransacao"] / freq_produto["idTransacao"].sum()

freq_produto["Freq. Rel. Acum."] = freq_produto["Freq. Rel."].cumsum()

freq_produto

#%%
df
#%%

freq_cat = df.groupby(["descCategoriaProduto"])[["idTransacao"]].count().rename(columns={"idTransacao":"Freq. Abs."})

freq_cat["Freq. Abs. Acum."] = freq_cat["Freq. Abs."].cumsum()

freq_cat["Freq. Relat"] = freq_cat["Freq. Abs."] / freq_cat["Freq. Abs."].sum()

freq_cat["Freq. Relat. Acum."] = freq_cat["Freq. Relat"].cumsum()

freq_cat