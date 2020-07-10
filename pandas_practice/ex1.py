import pandas as pd
from pandas import DataFrame, Series
from pathlib import Path
base_dir=Path(__file__).resolve().parent

df = DataFrame(pd.read_csv(str(base_dir)+"/file/csv2.csv"))

print(df.index)
for t in df.index:
    print(t)
#前几行数据
print(df.head(1))
#列名
print(df.columns)
#列名转list
col = df.columns.tolist()
print(col[1])

#各列的类型
# object -- 代表了字符串类型
# int -- 代表了整型
# float -- 代表了浮点数类型
# datetime -- 代表了时间类型
# bool -- 代表了布尔类型
print("========")
print(df.dtypes)
print("========")
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

def selectItem(df,item):
    """
    传入dataframe，查询item的位置，返回list，list中每项存[x,y]
    """
    coor = []
    l = []
    for indexs in df.index:
        for  i in range(len(df.loc[indexs].values)):
            if(df.loc[indexs].values[i] == item):
                l.append(indexs)
                l.append(i)
                coor.append(l)
                l = []
    return coor

def selectItemY(df,item,column):
    """
    传入dataframe，查询item在column的位置，返回list，list中每项存[y]
    """
    coor = []
    for indexs in df.index:
        if(df.loc[indexs,column] == item):
            coor.append(indexs)
    return coor

def selectItemX(df,item,line):
    """
    传入dataframe，查询item在line的位置，返回list，list中每项存[x]
    """
    coor = []
    for col in range(len(df.loc[line].values)):
        if(df.loc[line].values[col] == item):
            coor.append(col)
    return coor

def initDfCsv(file,fList):
    """
    传入文件和过滤的列，返回dataframe。
    如果fList传入[]，则返回全部数据
    """
    if fList == []:
        df = pd.read_csv(file,skipinitialspace=True)
    else:
        df = pd.read_csv(file,skipinitialspace=True, usecols=fList)
    return df

if __name__ == "__main__":
    c = selectItem(df,"serverB")
    print(c,"=============c")
    d = selectItemY(df,"serverB","SERVER")
    print(d,"=============d")
    e = selectItemX(df,"xx",0)
    print(e,"=============e")
    df1 = initDfCsv(str(base_dir)+"/file/csv2.csv",[])
    print(df1)