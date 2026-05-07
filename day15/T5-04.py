import pandas as pd
import matplotlib.pyplot as plt
import koreanfont
import seaborn as sns 
df_csv = pd.read_csv(
    './day15/titanic/train.csv', # 파일 경로
    header=0, # 시작할 행 개수 (0부터 시작)
    encoding='utf-8', # 인코딩(한글: utf-8, cp949, euc=kr) 파일마다 다름
    usecols=['Survived', 'Pclass', 'Sex', 'Age', 'Embarked'] ,# 특정한 열만 추출 기본값은 다가져옴
    na_values=[' ', '-', '미응답', 'N/A'], # 특정 값을 결측치 변환
    on_bad_lines='warn', # 만일 불러오는중 해당 행 오류 발생시 제외/패스
    )
df_csv.info()
# [1. 타이타닉 생존 데이터 분석]
# 출처: Kaggle - Titanic: Machine Learning from Disaster
# https://www.kaggle.com/competitions/titanic/overview

# [2. 가설]
# 가설 1: 여성과 아동의 생존율이 남성보다 월등히 높을 것이다. (사회적 보호 원칙)
# 가설 2: 높은 객실 등급(1등석)을 이용한 승객일수록 생존율이 높을 것이다. (경제적 지위와 안전의 상관관계)
# 가설 3: 특정 항구(사우샘프턴 등)에서 탑승한 승객은 객실 등급 분포에 따라 생존율 차이가 발생할 것이다.

# [3. 데이터 전처리]
# 수치형 결측치 보정: '나이(Age)' 컬럼의 결측치는 이상치에 강건한(Robust) 분석을 위해 중앙값(Median)으로 대체해야 한다.
df_csv['Age'] = df_csv['Age'].fillna(df_csv['Age'].median())
df_csv.info()
# 범주형 결측치 보정: '승선 항구(Embarked)' 컬럼의 결측치는 가장 빈번하게 등장하는 최빈값(Mode)으로 대체해야 한다.
df_csv['Embarked'] = df_csv['Embarked'].fillna(df_csv['Embarked'].mode()[0])
df_csv.info()




# [3. 데이터 시각화 및 분석]
# 3-1 : 생존 분포 분석: 전체 생존자와 사망자의 비중을 파악할 수 있는 sns.countplot 를 생성한다.
sns.countplot(df_csv, x='Survived').set_xticklabels(['사망', '생존'])
plt.title('생존 여부 분포')
plt.xlabel('생존 여부')
plt.ylabel('인원 수')
plt.show( )
# 3-2 : 연령대별 상세 분석:나이에 따른 생존/사망 분포를 히스토그램으로 시각화한다.데이터의 흐름을 파악할 수 있도록 커널 밀도 추정 곡선(KDE)을 포함한다.
sns.histplot(df_csv[df_csv['Survived']==0]['Age'], color='red', alpha=0.5, bins=15, kde=True, label='사망')
sns.histplot(df_csv[df_csv['Survived']==1]['Age'], color='skyblue', alpha=0.5, bins=15, kde=True, label='생존')
plt.legend()
plt.xlabel('나이')
plt.ylabel('인원 수')
plt.title('나이별 생존 분포')
plt.show()

# 3-4 (성별): sns.countplot을 사용하여 성별(Sex)에 따른 생존 여부(Survived)별 인원수를 시각화한다.
# sns.countplot(데이터, x= x축레이블, hue= 나누기기준)
sns.countplot(df_csv, x='Sex', hue='Survived').set_xticklabels(['남자', '여자'])
plt.xlabel('성별')
plt.ylabel('인원 수')
plt.legend(labels=['사망', '생존'])
plt.show()
# 3-5 (객실 등급): sns.countplot을 사용하여 객실 등급(Pclass)에 따른 생존 여부(Survived)별 인원수를 시각화한다.
sns.countplot(df_csv, x='Pclass', hue='Survived')
plt.xlabel('객실 등급')
plt.ylabel('인원 수')
plt.legend(labels=['사망', '생존'])
plt.show()

# 3-6 (승선 항구): sns.countplot을 사용하여 승선 항구(Embarked)에 따른 생존 여부(Survived)별 인원수를 시각화한다.
sns.countplot(df_csv, x='Embarked', hue='Survived')
plt.xlabel('승선 항구')
plt.ylabel('인원 수')
plt.legend(labels=['사망', '생존'])
plt.show()

