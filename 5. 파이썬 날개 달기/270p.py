from operator import itemgetter

# operator.itemgetter()는 인덱스나 키에 해당하는
# 항목을 추출하는 특정 함수를 반환한다.
# 이를 통해 특정 요소를 기준으로 학목을 정렬할 때 쓸 수 있다.
ssawadihao = [
    ('Minnie', 29, 'A'),
    ('Yuqi', 27, 'B'),
    ('Shuhua', 26, 'B'),
]

result = sorted(ssawadihao, key=itemgetter(1)) # 리스트 {ssawadihao}의 아이템인 각 튜플의 두 번째 요소를 기준으로 정렬
print(result)