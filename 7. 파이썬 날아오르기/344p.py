# 입력받은 데이터를 역순으로 호출하도록 할 수 있다.
# 원리는 MyIterator 클래스와 동일하다.
class ReversrIterator:
    def __init__(self, data):
        self.data = data
        self.position = len(data) - 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.position < 0:
            raise StopIteration
        result = self.data[self.position]
        self.position -= 1
        return result

if __name__ == '__main__':
    i = ReversrIterator([1, 2, 3])
    for item in i:
        print(item)