import pandas as pd
# 외부파일 판다스로 불러오기
# .csv 파일 불러오기
df_csv = pd.read_csv(
    './day14/data/data.csv', # 파일 경로
    header=0, # 시작할 행 개수 (0부터 시작)
    encoding='utf-8', # 인코딩(한글: utf-8, cp949, euc=kr) 파일마다 다름
    usecols=['사번', '이름', '나이', '부서'] ,# 특정한 열만 추출 기본값은 다가져옴
    na_values=[' ', '-', '미응답', 'N/A'], # 특정 값을 결측치 변환
    on_bad_lines='warn', # 만일 불러오는중 해당 행 오류 발생시 제외/패스
    dtype={'사번': str} # 특정한 열만 타입 지정 아니면 자동 dtype=str 전체
    )
print(df_csv)

# .excel 파일 불러오기 pip install openpyxl 필요
df_excel = pd.read_excel(
    './day14/data/data.xlsx',
    sheet_name='Sheet1', # 특정한 시트
    skiprows=0, # 시작할 행번호
)
print(df_excel)

# .json 파일 불러오기
df_json = pd.read_json('./day14/data/data.json')
print(df_json)
# .xml 파일 불러오기 pip install lxml 필요
df_xml = pd.read_xml(
    './day14/data/data.xml',\
    xpath='.//row' # xpath='.//가져올테그명'  .(현재파일뜻) //(파일전체에서찾기) row(마크업명)
    )
print(df_xml)


# 판다스 자료 외부파일 내보내기

# .csv 내보내기
df_xml.to_csv(
    './day14/data/data_out.csv', # 파일경로
    index=False, # 인덱스 제외
    encoding='utf-8', # 인코딩 지정
    na_rep='Unknown', # 결측값 치환
    header=True, # 헤더(열이름) 포함 여부
)
# .xlsx 내보내기
df_xml.to_excel(
    './day14/data/data_out.xlsx',
    sheet_name='회원정보', # 시트 이름 지정
)
# .json 내보내기
df_xml.to_json(
    './day14/data/data_out.json',
    orient='records', # 레코드(리스트) 형식으로 저장
    force_ascii= False, # 한글 유니코드 유지
    date_format='iso', # 날짜 형식을 표준 ISO(yyyy-mm-dd) 방식 지정
)
# .xml 내보내기
df_csv.to_xml(
    './day14/data/data_out.xml',
    index=False,
)