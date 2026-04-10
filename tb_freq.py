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