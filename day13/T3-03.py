import pandas as pd


# 판다스 병합,  merge(x,y, on ='공통컬럼명', how='inner/outer/left/right')
df_info = pd.DataFrame({'ID':[1,2,3], 'Name' : ['Ant', 'Bee', 'Cat']})
df_score = pd.DataFrame({'ID': [2,3,4], 'Score': [88,92,85]})

# 두 판다스 간에 ID가 같은(교집합) 자료 병합
result = pd.merge(df_info, df_score, on='ID', how='inner')
print(result)

result2 = pd.merge(df_info, df_score, on='ID', how='left')
print(result2)

result2 = pd.merge(df_info, df_score, on='ID', how='outer')
print(result2)

result2 = pd.merge(df_info, df_score, on='ID', how='right')
print(result2)

# 판다스 합치기 .concat([x,y], axis = 0(행)/1(열), ignore_index=True/False)
x = pd.concat([df_info,df_score], axis=0,ignore_index=True)
print(x) # 세로 연결

x = pd.concat([df_info,df_score], axis=1)
print(x) # 가로 연결

new_score = pd.Series([85,90,88], name='Score') # 새로운 열
df_info['NewScore'] = new_score
print(df_info)

# 정렬
x = {
    'Name' : ['Ant', 'Bee', 'Cat', 'Dog'],
    'Age' : [27,27,22,32],
    'Score' : [88,95,85,90]
}
df = pd.DataFrame(x)

# .sort_values(by='라벨명', ascending=True(오름차순)기본값/False(내림차순))
# .sort_values(by=[1차정렬, 2차정렬], ascending=[1차정렬, 2차정렬])
y = df.sort_values(by='Score', ascending=False) # 점수 기준 내림차순
print(y)

# 나이기준 오름차순 이후 점수 기준 내림차순 (나이 정렬후 동일한 나이끼리 점수 내림차순)
z = df.sort_values(by=['Age', 'Score'], ascending=[True, False])
print(z)

# 열이름(라벨) 내림차순으로 정렬
g = df.sort_index(axis=1, ascending=False)
print(g)


# 그룹  .groupby('그룹기준')['집계기준'].집계함수()
df = pd.DataFrame({
    'Category': ['A','A','B','B','A','B'],
    'Type' : ['X','Y','X','Y','X','Y'],
    'Values' : [10,20,30,40,50,60]
})

result = df.groupby('Category')['Values'].sum() # 카테고리 별 값 합계
print(result)

result = df.groupby('Type')['Values'].mean() # 타입 별 값 평균
print(result)

# 다중 그룹 .groupby([1차그룹, 2차그룹])[집계기준].집계함수
result = df.groupby(['Category', 'Type'])['Values'].sum() 
print(result)

result = df.groupby(['Category', 'Type'])['Values'].agg(['sum','mean','count']) # 다중 집계
print(result)