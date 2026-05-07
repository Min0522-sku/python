import pandas as pd
import matplotlib.pyplot as plt
import koreanfont
import json
import seaborn as sns

df_csv = pd.read_csv(
    './day15/team/train_HousePrices.csv', # 파일 경로
    header=0, # 시작할 행 개수 (0부터 시작)
    encoding='utf-8', # 인코딩(한글: utf-8, cp949, euc=kr) 파일마다 다름
    )
df_csv.info()
df_csv= df_csv.drop('Id', axis=1)

# 4. 데이터 전처리
# 4-1. 수치형 변수 결측치 처리
# 'LotFrontage', 'MasVnrArea', 'GarageYrBlt' 등의 수치형 변수의 결측치는 데이터의 중앙값(Median)으로 대체하여 보정한다.
df_csv['LotFrontage'] = df_csv['LotFrontage'].fillna(df_csv['LotFrontage'].median())
df_csv.info()
df_csv['MasVnrArea'] = df_csv['MasVnrArea'].fillna(df_csv['MasVnrArea'].median())
df_csv.info()
df_csv['GarageYrBlt'] = df_csv['GarageYrBlt'].fillna(df_csv['GarageYrBlt'].median())
df_csv.info()

# 4-2. 범주형 변수 결측치 처리 (정보 부재 명확)
# 정보 부재가 명확한 범주형 변수('Alley', 'PoolQC', 'Fence' 등)는 결측치를 'NoAlley', 'NoPool', 'NoFence'와 같이 특정 문자열로 대체한다.
df_csv['Alley'] = df_csv['Alley'].fillna('NoAlley')
df_csv.info()
df_csv['PoolQC'] = df_csv['PoolQC'].fillna('NoPool')
df_csv.info()
df_csv['Fence'] = df_csv['Fence'].fillna('NoFence')
df_csv.info()
df_csv['MiscFeature'] = df_csv['MiscFeature'].fillna('NoMisc')
df_csv.info()

# 4-3. 범주형 변수 결측치 처리 (일반)
# 아래 17개 주요 범주형 변수는 최빈값(Mode)을 활용하여 결측치를 일괄 보정한다.
# BsmtQual
# BsmtCond
# BsmtExposure
# BsmtFinType1
# BsmtFinType2
# Electrical
# FireplaceQu
# GarageType
# GarageFinish
# GarageQual
# GarageCond
# MSZoning
# Functional
# SaleType
# Exterior1st
# Exterior2ndMasVnrType
fill_list = [
    "BsmtQual",
    "BsmtCond",
    "BsmtExposure",
    "BsmtFinType1",
    "BsmtFinType2",
    "Electrical",
    "FireplaceQu",
    "GarageType",
    "GarageFinish",
    "GarageQual",
    "GarageCond",
    "MSZoning",
    "Functional",
    "SaleType",
    "Exterior1st",
    "Exterior2nd",
    "MasVnrType"
    ]
for i in fill_list:
    df_csv[i] = df_csv[i].fillna(df_csv[i].mode()[0])
df_csv.info()


# 5. 데이터 시각화 및 분석
# 5-1. 주택 판매 가격(SalePrice) 분포 분석
# sns.histplot을 사용하여 주택 판매 가격(SalePrice)의 분포와 치우침(Skewness) 정도를 확인한다. (KDE 포함)

# [차트 사진]
# [차트 해석]
# 5-2. 주거 면적과 가격 관계 분석 (가설 1 검증)
# sns.scatterplot을 사용하여 지상 주거 면적(GrLivArea)과 판매 가격(SalePrice) 간의 상관관계를 산점도로 분석한다.

# [차트 사진]
# [차트 해석]
# 5-3. 주택 스타일별 가격 분포 비교 (가설 2 검증)
# sns.boxplot을 사용하여 주택 스타일(HouseStyle)별 가격 분포와 이상치(Outlier)를 파악한다.

# [차트 사진]
# [차트 해석]
# 5-4. 주요 외관 요소별 가격 분포 비교 (가설 2 검증)
# sns.boxplot을 사용하여 지붕 스타일(RoofStyle) 및 외장재(Exterior1st)에 따른 가격 차이를 분석한다.

# [차트 사진]
# [차트 해석]

# 5-5. 상관관계 시각화 및 핵심 인자 도출 (가설 3 검증)
# sns.heatmap을 사용하여 수치형 변수 전체의 상관계수를 시각화하고한다.
df_int = df_csv.select_dtypes(include=['number'])
all_corr = df_int.corr()
top_feature_order = all_corr['SalePrice'].sort_values(ascending=False).index
ordered_corr = all_corr.loc[top_feature_order, top_feature_order]
plt.figure(figsize=(20, 15))
sns.heatmap( ordered_corr, cmap= 'Blues' , annot=True )
plt.show()
# [차트 사진]
# [차트 해석]
