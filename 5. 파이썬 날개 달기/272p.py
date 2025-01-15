from operator import attrgetter

class Ssawadihao:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

mys = [
    Ssawadihao('Minnie', 27, 'A'),
    Ssawadihao('Yuqi', 27, 'B'),
    Ssawadihao('Shuhua', 26, 'B'),
]

result = sorted(mys, key=attrgetter('age')) # Sswadihao 객체의 {age} 객체 변수로 정렬