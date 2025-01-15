import urllib.request # urllib는 URL을 읽고 분석할 때 사용하는 모듈이다.

def get_namuwiki(**name):
    resource = "https://namu.wiki/w/{}".format(name)
    with urllib.request.urlopen(resource) as s: # urlopen(): URL을 입력받아 해당 URL에 대한 HTTP 요청을 보네고 응답 데이터를 반환
        with open("./namuwiki_%s.html" %name, 'wb') as f: # html 파일 객체를 바이너리 쓰기 파일로 열기
            f.write(s.read()) # 응답 데이터 객체 {s}를 html 파일 객체에 씀

# 단, 위 코드는 나무위키 서버에서 금지된 접근이므로,
# HTTP Error 403 오류를 띄우며 액세스를 거부한다.