# 목표로 하는 기능을 수행하도록 코드 수정

import sys

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open("memo.txt", 'a') # '-a'를 키워드로 입력받을 시, 추가 모드로 텍스트 파일 열기
    f.write(memo) # 메모 내용 추가
    f.write('\n') # 메모 내용을 입력하고 자동으로 개행
    f.close()