import requests

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99');
rjson = r.json()
gus = rjson['RealtimeCityAir']['row']

for gu in gus:
    if gu['IDEX_MVL']<250:
        print(gu['MSRSTE_NM'], gu['IDEX_MVL'])
    

# - bs4: (beautifulsoup4) -> HTML 파싱을 편리하게.
# - requests -> 브라우저에서 엔터를 치는 효과. URL에 요청하기
# - 라이브러리 활용해서 크롤링하기
