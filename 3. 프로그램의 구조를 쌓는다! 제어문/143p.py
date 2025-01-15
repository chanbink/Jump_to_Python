# for문의 응용

marks = [90, 25, 67, 45, 80] # 학생들의 성적

num = 0 # {num}: 학생의 번호를 받을 변수
for mark in marks: # 성적 리스트 {marks} 내의 원소를 차례로 {mark}에 대입
    num = num + 1
    if mark >= 60:
        print("Student %d passed." %num)
    else:
        print("Student %d failed." %num)