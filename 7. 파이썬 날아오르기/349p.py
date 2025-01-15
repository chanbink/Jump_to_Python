import time

def longtime_job():
    print("job start")
    time.sleep(1)
    return 'done'

list_job = (longtime_job() for i in range(5)) # 제너레이터 표현식
print(next(list_job)) # 제너레이터 객체 {list_job}의 첫 번째 요소 호출

# 위와 같이 작성한 경우, 제너레이터 표현식은 함수를 정의하고 객체를 생성하는 행위일 뿐이다.
# 따라서, 별도로 함수를 호출하지 않을 경우, 아무런 작업도 수행하지 않는다.
# 결국 함수 호출 시에 필요한 작업만 수행하게 되는데, 이를 느긋한 계산(lazy evaluation)이라 한다.
# 이런 느긋한 계산 특성은 필요한 작업만 수행하여 효과적으로 작업할 수 있다는 장점이 될 수 있다.