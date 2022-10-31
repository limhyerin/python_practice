# http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109
html_doc = """
<html>
    <head>
        <title>TEST PAGE</title>
    </head>
    <Body>
        <h1>Hello World</h1>
    </Body>
</html>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, "html.parser")

print(soup.select("h1")) # 리스트로 결과 출력
print(soup.select("h1")[0]) #  리스트없이 출력
print(soup.select("h1")[0].string) # h1 없이 문자열만 출력

print(soup.select("title")) # 리스트로 결과 출력
print(soup.select("title")[0]) #  리스트없이 출력
print(soup.select("title")[0].string) 
