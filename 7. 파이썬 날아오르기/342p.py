# 클래스로 이터레이터를 구현할 수 있다.
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.position = 0 # 객체 내 요소의 위치를 저장하는 객체 변수
    
    def __iter__(self): # __iter__(): 해당 클래스로 생성한 객체를 반복 가능 객체로 만드는 메서드
        return self # 반복 가능 객체를 반환해야 하며, 일반적으로 클래스 자신의 객체를 반환한다.
    
    def __next__(self): # __next__(): 반복 가능 객체의 값을 차례로 반환, __iter__()가 구현했을 경우 반드시 구현해야 함
        if self.position >= len(self.data): # {position}이 객체 길이를 넘어설 경우
            raise StopIteration # StopIteration 예외 발생
        result = self.data[self.position] # 전달받은 반복 가능 객체의 특정 위치의 요소를 저장
        self.position += 1 # 요소를 저장하고 위치를 하나 올림
        return result # 저장한 요소를 반환

if __name__ == '__main__':
    i = MyIterator([1, 2, 3])
    for item in i: # 이터레이터에 for문이 수행되었거나, next()가 호출될 경우 __next__() 메서드가 반드시 호출된다.
        print(item)