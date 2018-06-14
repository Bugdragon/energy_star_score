import pandas as pd
import numpy as np

data = pd.read_excel('./describe.xls')
missing_columns = data[data['缺失值占比'] > 50]
missing_columns = missing_columns.T.columns # 缺失值占比大于50%的列删除
print(missing_columns)

data = pd.read_csv('./data/Energy_and_Water_Data_Disclosure_for_Local_Law_84_2017__Data_for_Calendar_Year_2016_.csv')
result = './data/Energy_and_Water_Data_cleaned.csv'
data = data.drop(columns = missing_columns)
data.to_csv(result)
