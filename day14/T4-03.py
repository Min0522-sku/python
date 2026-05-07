import matplotlib.pyplot as plt
import pandas as pd
import koreanfont
import json

# json 파일에서 특정할 열("customer_data") 만 가져와서 데이터 프레임 구성
with open('./day14/T5_data.json', 'r', encoding='utf-8') as json_file :
    data_json = json.load(json_file)
df_customer = pd.DataFrame(data_json['customer_data'])
print(df_customer.head())

# 데이터 분석/시각화
# 성별 과 연령대 로 그룹화 , df.groupby( [ '그룹기준' , '그룹기준' ] )
# 다수통계 df.agg( { '열이름' : '함수명' } )
# 여러개 그룹화할 경우에는 .reset_index() 함수 이용하여 *행번호* 붙인다.
newDf = df_customer.groupby(['성별', '연령대']).agg({'고객 수':'sum', '평균 구매 금액':'mean'}).reset_index()
print(newDf)
print(newDf['연령대']) # 남성 여성 포함하여 연령대
print(newDf['연령대'].unique()) # 남성 여성 포함하여 중복 제거된 연령대

# 연령대별(그룹) 총 고객수 세로 막대 그래프
plt.bar(
    newDf['연령대'].unique(),
    newDf.groupby(['연령대'])
    .agg({'고객 수':'sum'})['고객 수'],
    color='blue',
)
plt.xlabel('연령대')
plt.ylabel('총 고객수')
plt.legend()
plt.title('연령대별 누적 고객 수')
plt.show()
# 차트확인 : 30대가 비중이 가장 크고 , 50대 고객이 가장 적다

# 성별 + 연령대별(그륩) 세로막대 그래프
male_data = newDf[newDf['성별'] =='남성']
female_data = newDf[newDf['성별'] =='여성']
plt.bar(male_data['연령대'], male_data['고객 수'], label='남성 수', color='#0000ff')
# 만약 곂쳐 나오는 경우 : 아래 순서로 변경할 막대에 bottom = df[열이름] 앞으로 올릴 자료 대입한다
plt.bar(female_data['연령대'], female_data['고객 수'], label='여성 수', color='#ffff00', bottom=male_data['고객 수'])
plt.xlabel('연령대')
plt.ylabel('총 고객수')
plt.legend()
plt.title('성별 및 연령대별 누적 고객 수')
plt.show()
# 차트확인 : 남성/여성 모두 30대에서 고객 수가 확연히 크다, 또한 40~50대 여성 비율이 더 높다.

# 연령대별(그룹) '평균 구매 금액' 가로막대 그래프
# plt.barh() : 가로 막대
plt.barh(newDf['연령대'], newDf['평균 구매 금액'], color='red')
plt.xlabel('평균 구매 금액')
plt.ylabel('연령대')
plt.title('연령대별 평균 구매 금액')
plt.legend()
plt.show()

# 차트확인 : 40대가 가장 구매력이 큰 집단임을 시사, 10대가 가장 적은 구매력을 가진다.