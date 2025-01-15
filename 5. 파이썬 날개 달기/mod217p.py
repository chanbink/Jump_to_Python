def add(a, b):
    return a + b

def sub(a, b):
    return a - b

if __name__ == '__main__': # 파일을 직접 수행할 때만 참이 되는 조건문
    print(add(1, 4))
    print(sub(4, 2))

# {__name__}은 파이썬이 내부적으로 사용하는 특별한 변수이다.
# 만약, 터미널에서 파일을 직접 실행할 경우,
# 해당 파일의 {__name__} 변수에 자동으로 '__main__'이 저장된다.
# 하지만, 파이썬 셸이나 다른 모듈에서 이 파일을 import로 불러올 경우,
# 이 파일의 {__name__}에 모듈명인 'mod217p'가 저장된다.