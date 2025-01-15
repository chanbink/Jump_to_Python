gidle = ['Miyeon', 'Minnie', 'Soyeon', 'Yuqi', 'Shuhua']
snacks = ['candy', 'chocolate', 'jelly']

result = zip(gidle, snacks)
print(list(result)) # 개수가 짧은 리스트에 맞추어져, 긴 리스트의 뒤의 원소는 합쳐지지 못한다.