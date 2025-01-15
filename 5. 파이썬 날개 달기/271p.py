from operator import itemgetter

ssawadihao = [
    {'name':'Minnie', 'age':29, 'grade':'A'},
    {'name':'Yuqi', 'age':27, 'grade':'B'},
    {'name':'Shuhua', 'age':26, 'grade':'B'}
]

result = sorted(ssawadihao, key=itemgetter('age')) # 리스트 {ssawadihao}의 아이템인 딕셔너리의 키 'age'를 기준으로 정렬
print(result)