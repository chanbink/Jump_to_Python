f = open("C:/doit/new_file.txt", 'r')
lines = f.readlines() # readlines(): 파일의 모든 줄을 읽은 뒤 각 줄을 요소로 하는 리스트 반환
for line in lines:
    print(line)
f.close()