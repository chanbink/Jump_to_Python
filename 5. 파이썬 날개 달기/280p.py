def a():
    return 1 / 0 # 호출하면 ZeroDivisionError 발생

def b():
    a() # a()를 호축

def main():
    try:
        b() # b()를 호출
    except:
        print("Error occurred.")

main() # 호출 관계가 복잡할 경우, 언제 오류가 발생하는지 알기 어려움.