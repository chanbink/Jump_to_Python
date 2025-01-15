try:
    f = open("Minnie", 'r')

except FileNotFoundError: # 파일이 없을 경우, 아무것도 하지 않고 통과(오류 회피)
    pass