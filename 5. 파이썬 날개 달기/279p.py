import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working: %s\n" %i)

print('Start')

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join() # join(): 해당 스레드가 종료될 때까지 메인 스레드가 동작을 멈추고 대기하도록 지시.

print('End')