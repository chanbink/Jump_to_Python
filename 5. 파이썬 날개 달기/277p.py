import time

def long_task(): # 1초에 한 번씩 5번 메시지를 출력하는 함수(5초 소요)
    for i in range(5):
        time.sleep(1)
        print("working: %s\n" %i)

print('Start')

for i in range(5): # long_task() 함수를 5번 호출(총 25초 소요)
    long_task()

print('End')

# 컴퓨터에서 동작 중인 프로그램을 프로세스(process)라 한다.
# 한 개의 프로세스는 하나의 일만 수행한다.
# 이 프로그램은 long_task() 동작을 한 번에 하나씩 수행하므로, 25초가 소요된다.