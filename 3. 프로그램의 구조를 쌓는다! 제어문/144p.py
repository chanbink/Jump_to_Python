marks = [90, 25, 67, 45, 80]

num = 0
for mark in marks:
    num = num + 1
    if mark < 60:
        continue
    print('Student %d passed. Congratulations!' %num)
    # 조건을 만족하지 못하면 for문 처음으로 돌아가므로, 굳이 else를 사용할 필요가 없음