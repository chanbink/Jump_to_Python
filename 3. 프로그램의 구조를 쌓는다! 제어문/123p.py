money = True

if money:
    print('Take')
print('a') # 들여쓰기가 없으므로 if 블록 이탈
    print('taxi.') # 오류: if 블록에서 나왔으므로 들여쓰기를 하면 IndentationError 발생.