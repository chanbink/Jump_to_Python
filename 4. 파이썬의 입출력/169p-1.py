# 함수 안에서 함수 밖의 변수를 바꾸는 방법

a = 1
def vartest(a):
    a = a + 1
    return a # return을 사용하면 입력받은 값을 변경하고 반환하므로, 함수 밖에 영향을 행사할 수 있다.

a = vartest(a)
print(a)