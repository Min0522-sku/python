
import numpy as np

# .csv 파일 로드
#data = np.genfromtxt("파일경로", delimiter='구분문자', skip_header=제외할헤더(행)수)
data = np.genfromtxt("./day11/customer_purchase_data.csv", delimiter=',' , skip_header=1)
# 가져온 데이터의 넘파이 형식 확인
print(data.shape)

# 1
sales = data[:, 4]
print(sales)
# 평균
print(np.mean(sales))
# 총 매출액
print(np.sum(sales))

#2 조건 필터링
cont1 = data[:, -1] >= 20
cont2 = data[:, 4] >= 2000
result = data[cont1 & cont2]
print(result[:, 0])


#3 통계
arpv = data[:, 4] / data[ : , 1]
print(np.max(arpv))
findIndex = np.argmax(arpv)
print(data[findIndex, 0])

# 4
cont3 = (data[:,1]<=3) & (data[:,3]<=1)
print(np.sum(cont3))

# 5
data_min = np.min(data[:,4])
data_max = np.max(data[:,4])
print(data_min, data_max)

norm_data = (sales-data_min) / (data_max-data_min)
vip_data = norm_data >= 0.9
print(data[vip_data])

