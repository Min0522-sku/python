 
import asyncio # 비동기 라이브러리
from playwright.async_api import async_playwright # 동적 웹페이지 크롤링 라이브러리
import pandas as pd
# 동적페이지 크롤링

# url : https://search.naver.com/search.naver?where=image&query=%EB%A0%88%EC%A0%9C
# 박스 : tile_item
# 이미지 : _fe_image_tab_content_thumbnail_image
# 타이틀 : info_title

# 동기 웹크롤링
async def naverRun(): # 동기화된 함수
    # playwright 실행하고 p 변수에 결과 받기
    async with async_playwright() as p :
        # await(대기) 상태 이용한 크롬 실행
        # headless=False : 브라우저가 직접 실행된다 <봇차단 방지>
        browser = await p.chromium.launch(headless=False)

        # 실행된 브라우저(chromuim) 에서 새로운 페이지에 지정한 URL 대입하여 이동
        url = 'https://search.naver.com/search.naver?where=image&query=레제' # url
        page = await browser.new_page() # 새로운페이지 열기
        await page.goto(url)

        # 대기상태 만들기(자료가 표시될 때까지 기다리기)
        # 스크롤 내리기 이벤트(JS)
        for i in range(2): # 스크롤 2번 내리기
            # page.wait_for_timeout(밀리초) : 시스템(인터넷속도)에 따라 적절하게 설정
            await page.wait_for_timeout(3000)
            # await page.evaluate("JS 코드")
            # window.scrollTo(시작위치, 이동위치)
            # 이동위치 : document(현재html).body(본문).scrollHeight(스크롤높이) : 즉 현재 브라우저 스크롤을 본문의 가장 하단으로 이동
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

        


        # 실행된 페이지에서 특정한 요소 가져오기
        # page.query_selector_all(식별자) 여러개, page.query_selector(식별자) 한개
        items = await page.query_selector_all('.tile_item')
        image_list = []
        for item in items: # 여러개 item 에서 제목과 이미지 가져오기
            title_tag = await item.query_selector('.info_title .txt') # 제목
            image_title = await title_tag.inner_text() if title_tag else '제목없음' # <마크업> inner_text <마크업>
            image_tag = await item.query_selector('._fe_image_tab_content_thumbnail_image') # 이미지
            image_link = await image_tag.get_attribute('src') if image_tag else '이미지없음' # .get_attribute('속성명'), <마크업 속성명 = 값>

            image_list.append({'제목':image_title, '링크':image_link})
        print(image_list)    
        
        # (직접) 안전하게 브라우저 닫기
        await browser.close()

asyncio.run(naverRun()) # 동기화된 함수 실행