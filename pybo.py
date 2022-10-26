![코드](https://user-images.githubusercontent.com/70150896/197973530-9be591d3-1a40-441c-89a9-c8a98a7297ad.png)
![실행](https://user-images.githubusercontent.com/70150896/197973547-98002a3e-c95f-46da-a6bb-ad1c9ab97511.png)
![결과](https://user-images.githubusercontent.com/70150896/197973562-7fc7579b-ec2e-4daf-be11-7dc1763e85e4.png)

# 모듈 읽어 들임
from flask import Flask
from urllib import request
from bs4 import BeautifulSoup

# 웹 서버 생성
app = Flask(__name__)
@app.route("/")

def hello():
    # urlopen() 함수로 기상청의 전국 날씨를 읽습니다
    target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108") #기상청 html

    #BeautifulSoup를 사용해 웹 페이지를 분석합니다
    soup = BeautifulSoup(target, "html.parser")

    # location 태그를 찾습니다
    output = ""
    for location in soup.select("location"):
        output += "<h3>{}</h3>".format(location.select_one("city").string)
        output += "날씨:{}<br/>".format(location.select_one("wf").string)
        output += "최저/최고 기온: {}/{}"\
            .format(\
                location.select_one("tmn").string,\
                location.select_one("tmx").string\
            )
        output += "<hr/>"
    return output
