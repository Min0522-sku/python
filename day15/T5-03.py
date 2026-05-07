import pandas as pd
import matplotlib.pyplot as plt
import koreanfont
import json

with open('./day15/T5_data.json', 'r', encoding='utf-8') as json_file :
    data_json = json.load(json_file)
df = pd.DataFrame(data_json['financial_performance_data'])
print(df)

import seaborn as sns 
# 플롯박스 : '수익' '비용' '이익' 으로 박스플롯 표시
sns.boxplot(df, gap=0.5)
plt.ylabel('금액')
plt.title('항목별 금액 분포')
plt.show()


# 플롯박스 : 분기별 수익 데이터로 박스플롯 표시
# 플롯박스에서 그룹  df.boxplot(column=[값], by=그룹기준)
df.boxplot(column=['수익'], by='분기')
plt.show()

# 차트 확인 : 2분기가 수익 중앙값이 가장 높고, 
# 1분기가 박스가 길어 수익이 불안정함(불확실함), 
# 4분기가 박스가 짧아 조밀하게 있어서 수익성이 안정하다.
