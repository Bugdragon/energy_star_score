import pandas as pd
import numpy as np

data = pd.read_csv('./data/Energy_and_Water_Data_Disclosure_for_Local_Law_84_2017__Data_for_Calendar_Year_2016_.csv')
#print(data.head()) # 60列
#print(data.info())

data = data.replace({'Not Available': np.nan}) # np.nan可解释为数字
for column in list(data.columns):
    # 选择应为数字的列
    if('ft²' in column or 'kBtu' in column or 'Metric Tons CO2e' in column
            or 'kWh' in column or 'therms' in column or 'gal' in column or 'Score' in column):
        data[column] = data[column].astype(float) # 转换类型为float

data.to_csv('./data/Energy_and_Water_Data_explored.csv')

# 数据探索,describe()函数
result = './data/describe.xls'
explore = data.describe().T
explore['null'] = len(data) - explore['count']
explore['null(%)'] = explore['null'] / len(data) * 100
explore = explore[['null', 'max', 'min', 'null(%)']]
explore.columns = [u'缺失值', u'最大值', u'最小值', u'缺失值占比']
explore.to_excel(result)


