def mul(m):
    def wrapper(n): # 함수 mul()내부의 함수 wrapper() 정의
        return m * n # mul() 호출 시에 전달된 인자 {m}이 wrapper()에 저장하여 반환
    return wrapper # 외부 함수 mul()이 내부 함수 wrapper()를 반환

if __name__ == '__main__':
    mul3 = mul(3) # mul()은 wrapper()를 반환하므로 함수를 저장하는 것과 같은 효과이다.
    # 이는 파이썬의 함수 역시 객체이기 때문에 가능하다.
    mul5 = mul(5)

    print(mul3(10)) # mul()이 반환하는 것은 wrapper()이므로 이러한 사용이 가능하다.
    print(mul5(10))
# mul()과 같은 함수를 클로저(closure)라 한다.
# mul()이 wrapper()를 반환할 때, 인수로 받은 {m}은 wrapper()에 저장하여 반환한다.
# 클로저의 호출은 클래스가 특정 값을 설정하여 객체를 생성하는 과정과 유사하다.