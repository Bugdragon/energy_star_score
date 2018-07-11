import matplotlib.pyplot as plt
import pandas as pd

# Energy Star Score分布图
data = pd.read_csv('./data/Energy_and_Water_Data_cleaned.csv')
#print(data['ENERGY STAR Score'])
data = data.rename(columns = {'ENERGY STAR Score': 'score'})
plt.figure(figsize=(8, 8))
plt.style.use('fivethirtyeight')
plt.hist(data['score'].dropna(), bins=100, edgecolor = 'k')
# 正常显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.xlabel('能源之星分数') # x：分数
plt.ylabel('建筑物的数量') # y：数量
plt.title('能源之星分数分布图')
#plt.xlabel('Score')
#plt.ylabel('Number of Buildings')
#plt.title('Energy Star Score Distribution')
plt.show()

plt.figure(figsize=(8, 8))
plt.hist(data['Site EUI (kBtu/ft²)'].dropna(), bins=20, edgecolor='black')
plt.xlabel('Site EUI')
plt.ylabel('Count')
plt.title('Site EUI Distribution')
plt.show()

print(data['Site EUI (kBtu/ft²)'].describe())
print(data['Site EUI (kBtu/ft²)'].dropna().sort_values().tail(10))
print(data.loc[data['Site EUI (kBtu/ft²)'] == 869265, :])