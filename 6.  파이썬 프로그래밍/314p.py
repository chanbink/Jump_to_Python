# 필요한 기능은? 메모 추가, 메모 조회
# 입력받는 값은? 메모 내용, 프로그램 실행 옵션
# 출력하는 값은? memo.txt

# 계획: 아래 명령어를 실행했을 때, 메모를 추가할 수 있도록 한다.
# CWD> python 314p.py -a "I love (G)IDLE."
# -a는 실행 옵션, "I love (G)IDLE."은 추가할 메모 내용이다.

import sys

# sys.argv는 프로그램 실행 시 입력된 값을 읽어서 생성한 리스트이다.
option = sys.argv[1] # 실행 모드
memo = sys.argv[2] # 메모 내용

print(option) # 제대로 값을 입력받는지 확인
print(memo)