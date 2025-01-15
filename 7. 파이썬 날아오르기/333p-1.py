class Mul:
    def __init__(self, m):
        self.m = m
    
    def mul(self, n):
        return self.m * n
    
if __name__ == '__main__':
    mul3 = Mul(3) # 객체 생성과 동시에 생성자가 3을 인자로 받아 self.m에 3 전달
    mul5 = Mul(5)

    print(mul3.mul(10)) # mul() 메서드를 호출하고 10을 인자로 {n} 지역 변수에 전달
    print(mul5.mul(10))