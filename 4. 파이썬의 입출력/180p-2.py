f = open("C:/doit/new_file.txt", 'r')
for line in f: # 파일은 한 줄을 요소로 하는 반복 가능 객체이다. 반복문을 이용하여 파일을 읽을 수 있다.
    print(line)
f.close()