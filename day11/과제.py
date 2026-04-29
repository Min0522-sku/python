import numpy as np

data = np.genfromtxt("./day11/tbsh_gyeonggi_day_202512_안양시.csv", 
                     delimiter=',', 
                     skip_header=1, 
                     encoding='utf-8', 
                     dtype=None
                     )
print(data.shape)
#f2	행정동코드	분석의 기본 단위 (ID)
#f4	업종 대분류	'의료/건강' 데이터 필터링용
#f8	연령대	7(60대), 8(70대 이상) 필터링용
#f11	매출건수	비중 및 지수 계산의 핵심 수치

sorted_f2 = np.sort(data['f2']) # 행정동 코드를 정렬 (중복 제거를 위해)
areas = [sorted_f2[0]] # 행정동을 묶기 위한 리스트
# 중복 제거 로직
for i in range(1, len(sorted_f2)): # 정렬된 리스트를 돌며 인접한 행정동 코드 값이 다를때만 리스트에 추가
    if sorted_f2[i] != sorted_f2[i-1]:
        areas.append(sorted_f2[i])

ratio_list = [] # 동별 고령층 활동 비중을 담을 리스트
med_cnt_list = [] # 동별 의료 매출 건수를 담을 리스트
senior_sum_list = []
for dong in areas: # 묶어진 각 행정동을 순회
    dong_mask = (data['f2'] == dong) # 현제 동에 해당되는 행만 필터링 하는 마스크 
    dong_data = data[dong_mask] # 마스크를 사용해 해당 동 데이터만 추출

    senior_sum = np.sum(dong_data[dong_data['f8'] >=7]['f11']) # 'f8' >= 7 :70대 이상의 'f11' :매출건수 합계
    senior_sum_list.append(senior_sum)
    total_sum = np.sum(dong_data['f11']) # 해당 동 전체 매출 건수 합계
    ratio = senior_sum / total_sum if total_sum > 0 else 0 # 비중산출 전체 매출건수에서 고령층 매출건수가 차지하는 비율 예외처리
    ratio_list.append(ratio) # 결과저장

    med_sum = np.sum(dong_data[dong_data['f4'] == '의료/건강']['f11']) # 의료/건강인 데이터 매출 건수의  합계
    med_cnt_list.append(med_sum) # 결과 저장

ratios = np.array(ratio_list) # np 배열로 변환
med_cnt = np.array(med_cnt_list) # np 배열로 변환
senior_sum = np.array(senior_sum_list)

print("동별 고령층 활동 비중", ratios)
print("동별 의료 매출 건수", med_cnt)
# 스탭 1
med_avg = np.mean(med_cnt)
med_max = np.max(med_cnt)
print(f"평균값 : {med_avg}, 최댓값 : {med_max}")


# 스탭 2
threshold_A = np.sort(ratios)[int(len(ratios) * 0.8)] # 고령 비중 상위 20% 지점의 기준값 찾기
threshold_B = np.sort(med_cnt)[int(len(med_cnt) * 0.2)] # 의료 매출 건수 하위 20% 지점의 기준값 찾기

mask_a = (ratios >= threshold_A) # 고령 비중이 기준값 이상?
mask_b = (med_cnt <= threshold_B) # 의료 매출건수가 기준값 이하?
dong_cnt = np.sum(mask_a | mask_b) # 두 조건 중 하나라도 만족하는 행정동 개수 합산
print(f"취약/위험 그룹 행정동 수: {dong_cnt}개")

# 스탭 3
d = senior_sum/med_cnt
worst_idx = np.argmax(d)
worst_area_code = areas[worst_idx]
print(f"지수가 가장 높은 행정동 코드 : {worst_area_code}")

# 스탭 4
risk_mask = (ratios > np.mean(ratios)) & (med_cnt < np.mean(med_cnt)) # 고령 비중은 평균보다 높고, 동시에 의료 건수는 평균보다 낮은 구역 필터링
risk_percent = (np.sum(risk_mask)/ len(areas)) * 100 # 안양시 전체 행정동 중 복합 위험 지역이 차지하는 비율 계산
print(f"복합 위험 지역 비중: {risk_percent:.2f}%")

# 스탭 5
idx_min = np.min(d)
idx_max = np.max(d)

norm = (d-idx_min) / (idx_max - idx_min)

mask_1 = norm >= 0.9
p_areas = np.array(areas)[mask_1]
p_count = np.sum(mask_1)

print(f"최우선 관리 행정동 수 : {p_count}")
print(f"최우선 관리 대상 행정동 코드 : {p_areas}")