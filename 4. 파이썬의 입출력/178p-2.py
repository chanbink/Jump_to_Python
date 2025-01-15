f = open("C:/doit/new_file.txt", 'r')
while True: # 반복적으로 줄을 읽기 위해 무한 루프 실행.
    line = f.readline()
    if not line: break # 더 이상 읽을 줄이 없을 경우, readline()이 빈 문자열을 반환하므로 if문이 실행되어 루프를 탈출한다.
    print(line)
f.close()