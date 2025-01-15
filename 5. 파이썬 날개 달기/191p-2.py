# 한 프로그램에서 계산기 두 대가 필요하다면?
result1 = 0
result2 = 0 # 두 대의 계산기가 출력할 결괏값을 따로 정의

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num): # 같은 기능을 할 두 개의 함수를 따로 정의
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))

# 계산기가 여러 대 필요한 경우, 전역 변수와 함수가 계속 추가됨.
# 계산기 기능이 추가될 경우, 코드가 더욱 비대하고 가독성이 떨어짐.