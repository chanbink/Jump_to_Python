class Calculator: # 클래스 Calculator 정의
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator() # Calculator 클래스의 객체(object) 생성
cal2 = Calculator() # 계산기가 늘어나도 객체만 새로 생성하면 됨.

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))