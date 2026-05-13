import pandas as pd

# 서비스 클래스
class ItemService:
    # 생성자
    def __init__(self):
        self.df = pd.DataFrame([
            {'id': 1, 'name': '콜라', 'price':1000},
            {'id': 2, 'name': '사이다', 'price':1000},
            {'id': 3, 'name': '닥터페퍼', 'price':1500},
        ])
    
    # 함수
    # 개별조회 서비스
    def item(self, id):
        result = self.df[self.df['id'] == id]
        if result.empty:
            return "해당 상품이 없습니다"
        # df 타입 대신에 .to_json() 또는 .to_dict()
        return result.to_dict(orient= 'records')[0]
    
    # 전체조회 서비스
    def items(self):
        return self.df.to_dict(orient='records')
    
    # 저장 서비스
    def save(self, item):
        saveDf = pd.DataFrame([item]) # 저장할 객체를 데이터 프래임으로 만듬
        # 기존 데이터프레임에 새로운 데이터 프레임 연결
        self.df = pd.concat([self.df , saveDf], ignore_index=True)
        return True
    
    # 수정 서비스
    def update(self, item):
        update_id = item.get('id')
        if update_id not in self.df['id'].values:
            return "수정할 상품이 없습니다"
        else :
            idx = self.df[self.df['id'] == update_id].index
            self.df.loc[idx, item.keys()] = item.values()
            return True

    # 삭제 서비스
    def delete(self, id):
        if id not in self.df['id'].values:
            return "삭제할 상품이 없습니다"
        else:
            self.df = self.df[self.df['id'] != id]
            return self.df.to_dict(orient='records')
            
           

# **서비스 객체 생성**
item_service = ItemService()