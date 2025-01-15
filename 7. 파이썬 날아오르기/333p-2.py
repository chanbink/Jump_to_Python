class Mul:
    def __init__(self, m):
        self.m = m
    
    def __call__(self, n): # __call__(): 객체 자체를 함수처럼 호출하는 메서드
        return self.m * n

if __name__ == "__main__":
    mul3 = Mul(3)
    mul5 = Mul(5)

    print(mul3(10)) # 객체에 직접 인수 10을 전달
    print(mul5(10))