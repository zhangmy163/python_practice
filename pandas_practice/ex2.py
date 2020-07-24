import pandas as pd
from pandas import DataFrame, Series
from pathlib import Path
base_dir=Path(__file__).resolve().parent

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
    在列中查找，column为列的第一行列名
    传入dataframe，查询item在column的位置，返回list，list中每项存[y]
    可以用df.where()替换该方法
    """
    coor = []
    for indexs in df.index:
        if(df.loc[indexs,column] == item):
            coor.append(indexs)
    return coor

def selectItemX(df,item,line):
    """
    在行中查找，line为行的index号
    传入dataframe，查询item在line的位置，返回list，list中每项存[x]
    根据返回的值定位元素
    df.loc[line].values[x]
    这种查找不太常用
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

def addAnddel(df1,df2,target):
    """
    比较df1和df2两个dataframe的target(某一列里面各项)增减变化
    """
    for i in df1.index:
        item = df1.loc[i,target]
        # if selectItemY(df2,item,target) == []:  #性能太差循环太多，需要运行90多秒，而in values只需3秒
        if item not in df2[target].values:
            print(str(item) + "在df2中不存在")
    for i in df2.index:
        item = df2.loc[i,target]
        # if selectItemY(df1,item,target) == []:
        if item not in df1[target].values:
            print(str(item) + "在df1中不存在")

def changeItem(df1,df2,source,target):
    """
    比较df1和df2两个dataframe
    以source为准，检查target的变化情况
    比较的前提是source和target是唯一的，否则可能会报错
    """
    dfj=pd.merge(df1,df2,on=[source])
    for item in dfj[source]:
        # print(item,type(item),"============",selectItemY(df1,item,source),"====================",selectItemY(df2,item,source))
        #if df1.loc[selectItemY(df1,item,source)[0],target] != df2.loc[selectItemY(df2,item,source)[0],target]: # 如果selectItemY(df2,item,target)返回2个，即一对多时可能会有问题或判断不全；光使用这一行判断性能太差，嵌套循环太多
        # print(df1.shape,"=======1")
        #dropna()默认删除所有包含NaN的行，how='all'删除全是NaN的行
        data1 = sorted((df1.where(df1[source] == item).dropna(how='all'))[target].values)
        data2 = sorted((df2.where(df2[source] == item).dropna(how='all'))[target].values)
        # print(df1.shape,"=======2")
        # print(data1,"=========data1",item,data1)
        # print(data2,"=========data2",item,data2)
        if data1 != data2:
            print(str(item) + "在df2中有变化，以前",data1,"现在",data2)

if __name__ == "__main__":
    
    # print("===================车型对比=================")
    f1 = str(base_dir) + "/file/meta-car-model-filtered_old.csv"
    df1 = initDfCsv(f1,["modelID","brandName"]).drop_duplicates()
    # print(df1.index)
    f2 = str(base_dir) + "/file/meta-car-model-filtered_new.csv"
    df2 = initDfCsv(f2,["modelID","brandName"]).drop_duplicates()
    # print(df1.loc[11])
    # print(df2.loc[3672])
    # print(df1.where(df1["modelID"] == 5779).dropna().values)
    # print(df2.where(df2["modelID"] == 5779).dropna().values)
    

    # print("==================检查车型ID增减============")
    # addAnddel(df1,df2,"modelID")
    # print("==================检查车型名称变化============")
    # changeItem(df1,df2,"modelID","modelName")
    print("==================检查车型厂商名称变化============")
    changeItem(df1,df2,"modelID","brandName")
    # print("==================检查车型子级别变化============")
    # changeItem(df1,df2,"modelID","levelName")
    # print("==================检查车型国别变化============")
    # changeItem(df1,df2,"modelID","nation")
    # print("==================检查车型品牌名称变化============")
    # changeItem(df1,df2,"modelID","mainBrandName")
    # print("==================检查车型父级别变化============")
    # changeItem(df1,df2,"modelID","categoryName")
    # print("==================检查车型动力子级别变化============")
    # changeItem(df1,df2,"modelID","powerName")
    # print("==================检查车型动力父级别变化============")
    # changeItem(df1,df2,"modelID","powerCategoryName")
    # print("==================检查车型品牌类型变化============")
    # changeItem(df1,df2,"modelID","brandLevelName")
    # print("==================检查车型厂商类型变化============")
    # changeItem(df1,df2,"modelID","ventureName")
    # print((df1.where(df1["modelID"] == 4633).dropna())["mainBrandName"].values)
    # print((df2.where(df2["modelID"] == 4633).dropna())["mainBrandName"].values)
    # print("==================检查车型BBS mapping变化============")

    # f1 = str(base_dir) + "/file/old/cal/meta-bbs-car-model-mapping.csv"
    # df1 = initDfCsv(f1,[]).drop_duplicates()
    # # print(df1.index)
    # f2 = str(base_dir) + "/file/new/cal/meta-bbs-car-model-mapping.csv"
    # df2 = initDfCsv(f2,[]).drop_duplicates()
    # print("=================检查BBS增减=====================")
    # addAnddel(df1,df2,"bbsID")
    # print("=================检查变化========================")
    # changeItem(df1,df2,"modelID","bbsID")
