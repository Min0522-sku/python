import pandas as pd
import matplotlib.pyplot as plt
import koreanfont
import json

with open('./day15/T5_data.json', 'r', encoding='utf-8') as json_file :
    data_json = json.load(json_file)
df = pd.DataFrame(data_json['risk_return_data'])
print(df)

# 산점도 : 리스크 대비 수익률
plt.scatter(df['리스크'],df['수익률(%)'], c= 'skyblue', s=df['수익률(%)']*100, alpha=0.5)
plt.xlabel('리스크')
plt.ylabel('수익률')
plt.title('리스크 대비 수익률')
plt.grid()
plt.show()

# 산점도 : 자산(유형)별 리스크 대비 수익률
categories = df['자산'].unique()
print(categories)
for i, category in enumerate(categories):
    sub = df[df['자산'] == category]
    plt.scatter(sub['리스크'], sub['수익률(%)'], label=category)

plt.legend()
plt.show()