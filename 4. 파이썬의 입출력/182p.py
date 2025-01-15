with open("foo.txt", 'w') as f: # with: 리소스를 관리하거나, 작업의 시작과 종료를 명확히 정의할 때 사용하는 예약어.
    f.write("Life is too short, you need python.") # 쓰기가 완료되어 블록을 벗어날 때, 파일을 자동으로 닫음.