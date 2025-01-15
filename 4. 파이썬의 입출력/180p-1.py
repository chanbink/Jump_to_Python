f = open("C:/doit/new_file.txt", 'r')
data = f.read() # read(): 파일 내용 전체를 읽어 문자열로 반환
print(data)
f.close()