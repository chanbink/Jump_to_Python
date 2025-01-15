import time

def elapsed(original_func): # 함수를 입력받은 클로저 elapsed() 정의
    def wrapper(): # 내부 함수 wrapper() 정의
        start = time.time()
        result = original_func() # 입력받은 함수를 실행
        end = time.time()
        print("Function execution time: %f sec" %(end - start))
        return result # 입력받은 함수 수행 결과를 반환
    return wrapper # 내부 함수 wrapper() 반환

def myfunc(): # 메인 수행 함수 myfunc() 정의
    print("Function is executed...")

decorated_myfunc = elapsed(myfunc) # elapsed()는 함수 myfunc()를 받고
decorated_myfunc() # 두 함수의 기능을 모두 수행한다.

# 클로저는 기존 함수에 기능을 붙이기 편하다.
# 이를 활용하면, 기존 함수의 기능을 유지하며, 클로저의 기능을 덧붙일 수 있다.
# 따라서, 클로저는 기존 함수를 '장식'하는 것과 같은데,
# 이러한 클로저를 데코레이터(decorator)라 한다.