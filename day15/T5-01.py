import pandas as pd
import matplotlib.pyplot as plt
import koreanfont
import json

with open('./day15/T5_data.json', 'r', encoding='utf-8') as json_file :
    data_json = json.load(json_file)
df = pd.DataFrame(data_json['patient_status_data'])
print(df.head())

# 막대차트: 상태별 환자수 비교 
plt.bar(df['상태'], df['환자 수'])
plt.title('상태별 환자 수 비교')
plt.show()

# 원형차트: 전체대비 각 상태의 환자수 비율
# 백분율 

plt.pie(df['환자 수'], labels=df['상태'], autopct='%.2f%%', startangle=90)
plt.title('환자 상태 비율')
plt.show()
