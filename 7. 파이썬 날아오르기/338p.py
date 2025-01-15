import time

def elapsed(origin_func):
    def wrapper(*args, **kwargs): # wrapper()가 매개변수를 받도록 지정
        start = time.time()
        result = origin_func(*args, *kwargs) # {args}와 {kwargs}를 입력 인수로 지정 
        end = time.time()
        print("Function execution time: %f sec" %(end - start))
        return result
    return wrapper

@elapsed
def myfunc(msg):
    """데코레이터 확인 함수"""
    print("'%s' is printed." %msg) # {msg}에 내용을 전달받아 출력

myfunc('Minnie') # myfunc()에 문자열 'Minnie'를 입력

# 문자열 'Minnie'는 wrapper()함수의 {args} 매개변수로 전달된다.
# wrapper()가 작동하여 원래 함수가 호출되면, 원래 함수가 받은 인수들은 그대로 전달된다.