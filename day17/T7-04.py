
import asyncio # 비동기 라이브러리
from playwright.async_api import async_playwright # 동적 웹페이지 크롤링 라이브러리
import pandas as pd


# 크롤링 웹페이지
#  https://web.joongna.com/search/레드윙?page=1

# 동기화 함수 선언
# async def 함수명():
async def joongnaRun(): 
    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto('https://web.joongna.com/search/레드윙?page=1')

        await page.wait_for_load_state('networkidle') # networkidle : 통신이 모두 종료상태

        # 특정한 검색창 활용
        await page.get_by_placeholder('최소 가격').fill("10000") # '최소 가격' 입력상자에 10000 넣어주기
        await page.wait_for_timeout(1000)
        await page.get_by_placeholder('최대 가격').fill("300000") # '최대 가격' 입력상자에 300000 넣어주기
        await page.wait_for_timeout(1000)
        # 버튼클릭이벤트 , 특정한 식별자가 없는 경우에 버튼에 보이는 이름으로 가져올 수 있음
        apply_button = page.get_by_role('button', name='적용')
        await apply_button.click()
        await page.wait_for_timeout(3000)
        # 선택자 : a[href^="/링크"] 해당 링크로 시작하는 링크
        items = await page.query_selector_all('div.group > div > a[href^="/product/"] ')
        
        for item in items:
            title_tag = await item.query_selector('span')
            title = await title_tag.inner_text() if title_tag else '제목없음'

            price_tag = await item.query_selector("span.text-18")
            price = await price_tag.inner_text() if price_tag else '가격없음'
            print(title, price)

# 동기 함수 실행
# asyncio.run(동기함수())
asyncio.run(joongnaRun())