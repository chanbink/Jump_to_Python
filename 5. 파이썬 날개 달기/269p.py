import functools

data = [1, 2, 3, 4, 5]
result = functools.reduce(lambda x,y : x+y, data) # 왼쪽부터 차례로 요소를 더함.
# functools.reduce() 함수는 람다 함수와 같이 사용하기 좋다.

print(result)