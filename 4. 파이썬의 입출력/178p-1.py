f = open("C:/doit/new_file.txt", 'r') # 읽기 모드로 파일 열기
line = f.readline() # readline(): 파일의 한 줄을 읽는 함수. 파일의 첫 줄부터 읽게 된다.
print(line) # 문장 끝의 '\n'도 같이 읽으므로, 빈 줄이 같이 출력된다.
f.close()