def positive(x):
    return x > 0 # 양수를 입력받으면 True, 아니면 False를 반환

print(list(filter(positive,[1,-3,2,0,-5,6]))) # 246p-1.py보다 코드가 더 간결해졌다.