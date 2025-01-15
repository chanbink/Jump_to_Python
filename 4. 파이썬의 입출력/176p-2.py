f = open("C:/doit/new_file.txt", 'w')
for i in range(1, 11):
    data = "This is line %d.\n" %i
    f.write(data) # write(): 쓰기 모드나 추가 모드로 열린 파일에 입력 받은 데이터를 쓰는 함수
f.close()