def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i) # 양수들만 걸러서 리스트 {result}에 포함.
    return result

print(positive([1,-3,2,0,-5,6]))