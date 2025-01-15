import traceback # traceback은 쉬운 오류 추적을 도와주는 모듈이다.

def a():
    return 1 / 0

def b():
    a()

def main():
    try:
        b()
    except:
        print("Error occurred.")
        print(traceback.format_exc()) # traceback.format_exc(): 오류 추적 결과를 문자열로 반환

main()