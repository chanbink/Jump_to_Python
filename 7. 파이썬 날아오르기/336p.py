import time

def elapsed(origin_func):
    def wrapper():
        start = time.time()
        result = origin_func()
        end = time.time()
        print("Function execution time: %f sec" %(end - start))
        return result
    return wrapper

@elapsed # 함수 바로 위에 '@+클로저_이름'을 적으면 클로저를 데코레이터로 인식한다.
def myfunc():
    print("Function is executed...")

# 데코레이터 선언을 한 순간, myfunc()은 elapsed를 데코레이터로 하여 실행된다.
# decorated_myfunc = elapsed(myfunc)
# decorated_myfunc()