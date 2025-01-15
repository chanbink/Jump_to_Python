# 계산기 프로그램을 만들며 클래스 알아보기
result = 0 # {result}: 결과로 내보낼 값을 저장할 변수

def add(num):
    global result # 전역 변수 {result}에 함수에서 접근하여 덧셈을 계산
    result += num # {result}에 {num}을 더함
    return result # 결괏값 반환

print(add(3))
print(add(4)) # {result}가 전역 변수이므로 add()를 재호출하면 값이 더해짐