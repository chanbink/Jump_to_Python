import time

def longtime():
    print("Job start")
    time.sleep(1)
    return 'done'

list_job = [longtime() for i in range(5)] # 리스트 컴프리헨션
# 5초의 시간 소요
print(list_job[0]) # 리스트를 만들되, 성공 여부를 확인하기 위해 첫 번째 요소만 선택해서 출력하고 싶음.

# 위와 같은 코드를 사용할 경우, 리스트를 만드는 작업을 모두 수행한 후에 출력해야 하므로,
# 해당 작업에 걸리는 시간 5초를 모두 기다리고 하나의 요소만을 출력한다.