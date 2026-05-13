import pandas as pd

# 서비스 클래스
class StatsService:
    # 생성자
    def __init__(self):
        self.df = pd.read_csv('day19/project/data/books.csv',encoding='utf-8-sig')
    
    # 함수
    def all(self):
        result = {   
            "평균가격": int(self.df['가격'].mean()),
            "최고가격": int(self.df['가격'].max()),
            "최저가격": int(self.df['가격'].min()),
            "최다출판연도": int(self.df.groupby('출판년')['출판년'].count().idxmax())}
        return result
    
            
           

# **서비스 객체 생성**
stats_service = StatsService()