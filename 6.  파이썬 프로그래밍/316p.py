# 315p.py에 메모 출력 기능을 넣어보자.
# 계획: 315p.py의 기능은 유지하고, 아래의 명령어로 메모를 출력할 수 있도록 한다.
# CWD> python 316p.py -v

import sys

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open("memo.txt", 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open("memo.txt") # 디폴트 열기 모드는 읽기 모드이다.
    memo = f.read() # 메모 내용을 변수에 저장
    f.close()
    print(memo) # 저장된 메모 내용을 출력