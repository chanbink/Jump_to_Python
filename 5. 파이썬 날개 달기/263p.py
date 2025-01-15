import random

def random_pop(data): # 리스트를 입력받음
    number = random.randint(0, len(data) - 1) # 임의의 정수를 받아 인덱스로 함
    return data.pop(number) # 받은 인덱스를 반환하고 리스트에서 삭제

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data:
        print(random_pop(data))