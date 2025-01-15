# 목표: 탭(Tab)을 스페이스(Space) 4개로 바꾸기
# 필요한 기능은? 문서 파일 읽기, 문자열 변경하기
# 입력받는 값은? 탭을 포함하는 문서 파일
# 출력하는 값은? 탭이 공백으로 수정된 문서 파일

# 계획: 아래 명령어를 실행했을 때, 탭을 공백으로 바꾼 파일을 내놓아야 한다.
# CWD> python 319p-1.py src dst
# {src}: 원본 파일 이름, {dst}: 수정된 파일 이름

import sys

src = sys.argv[1]
dst = sys.argv[2]

print(src) # 키워드를 제대로 받는지 확인
print(dst)