try: # 일단 코드 실행
    4 / 0 # ZeroDivisionError 발생

except ZeroDivisionError as e: # ZeroDivisionError가 발생하면 except 블록 실행
    # {e}는 오류의 내용을 저장하는 변수이다.
    print(e)