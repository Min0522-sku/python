import pandas as pd
import matplotlib.pyplot as plt
import koreanfont
import json

with open('./day14/T5_data.json', 'r', encoding='utf-8') as json_file :
    data_json = json.load(json_file)
df_stock = pd.DataFrame(data_json['stock_data'])
print(df_stock.head())

# '기간' 별 '주가'와 '평균 이동선(3개월)' 선그래프 표현하고 '거래량'을 보조축(오른쪽 축)
fig, axs = plt.subplots()
axs.plot(df_stock['기간'], df_stock['주가'], label='주가', color='#ffff00')
axs.set_xlabel('기간')
axs.set_ylabel('주가')

axs.plot(df_stock['기간'], df_stock['평균 이동선(3개월)'], label='평균이동선(3개월)', color='#ff0000')

# ***보조축 : 오른쪽 세로축 *** 기본축.twinx()
axs2 = axs.twinx()
axs2.bar(df_stock['기간'], df_stock['거래량'], label='거래량', color='#000000', alpha=0.3)
axs2.set_ylabel('거래량')

fig.suptitle('기간별 주가 및 겨래량 추세')

plt.show()

# '주가', '거래량', '평균 이동선(3개월)' 간의 상관관계를 히트맵 표현(상관계수)
import seaborn as sns

matrix = df_stock[['주가', '거래량', '평균 이동선(3개월)']].corr()
# 상관 계수를  히트맵으로 시각화
sns.heatmap(matrix, cmap='coolwarm', annot=True, fmt='.2f')
plt.title('변수들 간의 상관관계')
plt.show()