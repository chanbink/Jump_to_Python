def gugu(n):
    result = [] # 결과 담을 리스트 생성
    result.append(n*1) # append()로 리스트에 값을 하나씩 담음
    result.append(n*2)
    result.append(n*3)
    result.append(n*4)
    result.append(n*5)
    result.append(n*6)
    result.append(n*7)
    result.append(n*8)
    result.append(n*9)
    return result # 결과 리스트를 반환

print(gugu(2))