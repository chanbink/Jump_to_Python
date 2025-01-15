import time

def elapsed(origin_func):
    def wrapper():
        start = time.time()
        result = origin_func() # 받은 함수를 인수 없이 실행
        end = time.time()
        print("Function execution time: %f sec" %(end - start))
        return result
    return wrapper

@elapsed # elapsed()를 myfunc()의 데코레이터로 지정
def myfunc(msg):
    print("%s is printed." %msg) # {msg}에 내용을 전달받아 출력

myfunc('Minnie') # 오류: wrapper()는 전달받은 myfunc()을 인수 없이 실행함.