
import pandas as pd
from pandas import DataFrame, Series
from numpy import nan as NaN
# df = pd.DataFrame(columns = ['modelID','type','source','target'])
# sf = pd.DataFrame([[1,"新增",None,None],[2,"减少",None,None]],columns = ['modelID','type','source','target'])
# tf = pd.DataFrame([[1,"修改","1","2"],[2,"修改","2","3"]],columns = ['modelID','type','source','target'])
# print(sf)
# print(tf)
# modelID1=1
# type1="新增"
# modelID2=2
# type2="修改"
# source2=2
# target2=3
# df = df.append(pd.DataFrame({"modelID":[modelID1],"type":[type1]}), ignore_index=True) 
# df = df.append(pd.DataFrame({"modelID":[modelID2],"type":[type2],"source":[source2],"target":[target2]},
# {"modelID":[modelID2],"type":[type2],"source":[source2],"target":[target2]}), ignore_index=True) 
# print(df)

# print(pd.merge(sf,tf,on=["modelID"]))

# df1 = pd.merge(sf,tf,how='outer')
# print(df)

df1=pd.DataFrame([[1,2,3],[NaN,NaN,2],[NaN,NaN,NaN],[8,8,NaN]])
print(df1)
print("=============")
print(df1.dropna())
#https://blog.csdn.net/dili8870/article/details/101506554
print(df1.dropna(how='all'))