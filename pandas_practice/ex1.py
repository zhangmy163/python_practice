import pandas as pd
from pandas import DataFrame, Series
from pathlib import Path
base_dir=Path(__file__).resolve().parent

df = DataFrame(pd.read_csv(str(base_dir)+"/file/csv2.csv"))

# print(df.index)
# for t in df.index:
    # print(t)
#前几行数据
print(df.head(1))
#列名
print(df.columns)
#列名转list
col = df.columns.tolist()
labels = list(df.columns.values)
print(col[1])

#各列的类型
# object -- 代表了字符串类型
# int -- 代表了整型
# float -- 代表了浮点数类型
# datetime -- 代表了时间类型
# bool -- 代表了布尔类型
# print("========")
# print(df.dtypes)
# print("========")
#选则单行，单行单列可以tolist()
print(df.loc[2].tolist())

#选则多行
print(df.loc[1:2])

#取一列
print(df['IP_ADDRESS'].tolist())
print(df['IP_ADDRESS'].values)
print(df.loc[0].values,"=============values")

# 取列
print(df.loc[:,'IP_ADDRESS'])

print(df.loc[:,'IP_ADDRESS'].values)

# 取确定的点
print(df.loc[0].values[2],"==================loc")

# where
print(df.where(df["SERVER"] == "serverA").dropna().sort_index())
print(df.where(df["SERVER"] == "serverA").dropna()["IP_ADDRESS"].values)
print(df.where(df["SERVER"] == "serverA").dropna())

# 行列数
print(df.shape)

print(df)
#删除列
df1=df.drop(columns=["SERVER"])
print(df1)
#删除行
df2=df.drop(index=[3])
print(df2)
#重命名列
df3 = df.rename(columns={'SERVER': 'SName'}, inplace=True)
print(df3)
