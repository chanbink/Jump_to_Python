# 목표로 하는 기능을 수행하도록 코드 수정

import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read() # 원본 파일을 읽고 내용을 저장
f.close() # 내용을 저장했으니, 원본 파일은 더 이상 볼 일 없음

space_content = tab_content.replace('\t', ' '*4) # replace(): 문자열의 특정 내용을 다른 내용으로 변경
print(space_content) # 바뀐 내용이 출력되나, 탭과 공백의 크기가 같으므로 확인은 어렵다.