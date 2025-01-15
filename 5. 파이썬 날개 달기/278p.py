import time
import threading # threading은 스레드  프로그래밍(thread programming)을 위한 모듈이다.
# 스레드(thread)는 CPU가 작업을 처리하는 최소 단위를 말한다.

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working: %s\n" % i)

print('Start')

threads = [] # 스레드를 담을 리스트 생성
for i in range(5):
    t = threading.Thread(target=long_task) # long_task() 함수를 실행하기 위한 스레드 객체를 생성
    threads.append(t) # 각 스레드를 리스트에 추가

for t in threads:
    t.start() # start(): 각 스레드를 실행

print('End')

# 이 프로그램을 실행 시, 각 스레드에서 long_task()를 동시에 실행하므로, 약 5초의 시간이 소요된다.
# 이 때, 'End'가 먼저 출력되고 long_task()가 실행되는 것을 볼 수 있는데,
# 이는 스레드의 작업은 서로 동기화 없이 실행되기 때문이다.

# 프로그램이 시작되면 자동으로 생성되는 스레드를 메인 스레드(main thread)라 한다.
# 이 프로그램이 실행되는 동시에 메인 스레드가 생성되어 작업이 진행된다.
# threading.Thread()로 스레드 객체를 생성할 경우, 5개의 서브 스레드(sub thread)가 생성된다.
# 각 스레드는 long_task()를 start() 함수에 의해 작업을 시작하지만,
# 이는 메인 스레드의 개별 작업에 영향을 주지 않는다.
# 따라서, 서브 스레드의 실행 이후, 즉시 메인 스레드는 'End'를 출력하고,
# 서브 스레드의 작업 종료를 기다린다.

# 위의 문단을 도식화 하면 다음과 같다.
# 메인 스레드: ... 'Start' 출력 -> 서브 스레드 생성 -> 서브 스레드 실행 -> 'End' 출력 -> 서브 스레드 종료까지 대기
# 서브 스레드:                                                         -> 반복문 수행