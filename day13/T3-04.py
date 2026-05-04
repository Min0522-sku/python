import matplotlib as mpl
print(mpl.__version__)
# 차트내 한글 깨짐 방지 코드 + 한글 폰트
mpl.rc('font', family='Malgun Gothic') # 또는 'Noto Sans CJK JP'
mpl.rcParams['axes.unicode_minus'] = False


# 시각화 데이터 분석 격과를 시작적으로 

# 선 그래프
import matplotlib.pyplot as plt
# 그래프 데이터 준비
x = [0,1,2,3,4,5,6,7,8,9] # x축 (가로축의 값)
y = [9,8,7,6,5,4,3,2,1,0] # y축 (세로축의 값)
# 그래프 설정
plt.plot(x,y) # .plot(x값, y값)
plt.title('Line Chart Exam') # .title('차트제목')
plt.xlabel('X-axis Title') # .xlabel('x축 제목')
plt.ylabel('Y-axis Title') # .ylabel('y축 제목')
plt.grid(True) # 눈금선 표시
# 그래프 출력
plt.show()

# 선 그래프 2
y2 = [0,1,2,3,4,5,6,7,8,9]
plt.plot(x,y, label='감소하는 선(범례명)', color = 'blue', linestyle=':')
plt.plot(x, y2, label='증가하는 선(범례명)', color ="#FF0000", linestyle=':')
plt.legend() # 범례에 항목명 표시
plt.show()

# 막대 그래프 .bar(x축, y축, width= 굴기, label='항목명', color='색상)
categories = ['학생1', '학생2', '학생3', '학생4'] 
values = [80, 92, 78, 90]
values2 = [88, 91, 75, 85]
# 막대 곂치지 않게 표시
import numpy as np
x = np.arange(len(categories)) # 0 부터 x축의 값 개수 만큼 생성 0~3

plt.bar(x - 0.2, values, width=0.4, label='국어성적', color='blue')
plt.bar(x + 0.2, values2, width=0.4, label='수학성적', color='orange')
plt.title('학생 성적 비교')
plt.xlabel('학생명')
plt.ylabel('성적점수')
plt.legend()
plt.grid(axis='y') # 눈금선 (y축만)
plt.xticks(x, categories) # 위치 순으로 라벨 지정
plt.show()

# 파이 그래프 백분율   .pie(값, labels=항목명, colors='색상', explode='강조', startangle=시작각도, autopct='비율표시')

labels = ['피자', '햄버거', '샐러드', '파스타']
sizes = [40,30,20,10]
colors = ['gold','lightcoral','lightskyblue','lightgreen']
explode = [0.1,0,0,0] # 원형에서 튀어나오는 정도(강조)
plt.pie(sizes,labels=labels,colors=colors,explode=explode,startangle=90,autopct='%1.1f%%')
# %형식문자%자릿수.소수자릿수f ,f실수. %% 형식문자가아닌 % 표시
plt.show()

#선점도, 밀집도,    .scatter(x축값, y축값, c(color)=색상, s(size)= 점크기)
x = [1.5,2.5,3.5,4.5,5.5]
y = [50,60,65,70,75]
plt.scatter(x,y, c= 'red', s=50)
plt.grid()
plt.show()

# 히스토그램, 상관관계,  .hist(값, color='색상', alpha=투명도, bins=구간개수)
data = []
for i in range(50):
    value = sum([(i * j) % 100 / 100 for j in range(1,13)])
    data.append(value)

plt.hist(data, color='skyblue', alpha=0.5, bins=30)
plt.show()


# 다중 그래프 .subplots(행, 열)

fig, axs = plt.subplots(1, 2, figsize=(10,7))
# fig : 다중그래프를 가지고 있는 전체 그래프
# axs : 다중그래프의 위치, axs[0] 첫번째 그래프, axs[1] 두번째 그래프
# figsize =(가로, 세로) 전체 그래프의 가로inch, 세로inch
axs[0].plot([1,2,3],[1,4,9])
axs[0].set_title('선 그래프') # .title 전체 그래프의 제목 .set_title 하위 그래프의 제목
axs[0].set_xlabel('x축제목')
axs[0].set_ylabel('y축제목')
axs[1].bar([1,2,3],[3,5,2])
axs[1].set_title('막대 그래프')
axs[1].set_xlabel('x축제목')
axs[1].set_ylabel('y축제목')

# 그래프 이미지(png) 다운로드 .savefig('파일경로')
plt.savefig('./day13/save_chart.png')
plt.show()




