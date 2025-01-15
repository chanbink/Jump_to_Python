try:
    f = open("foo.txt", 'w')
    f.write("I love Minnie.")
    4 / 0 # ZeroDivisionError 발생

finally:
    print("Error occurred.") # 오류가 발생해도 무조건 실행. 단, 오류 메시지는 출력된다.
    f.close()