# 확장자가 .py인 파일만 검색하도록 코드 변경

import os

def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        ext = os.path.splitext(full_filename)[-1] # os.path.splitext(): 파일 이름을 확장자 기준으로 이름과 확장자로 나누어 튜플로 반환
        if ext == ".py": # 튜플의 마지막 요소(확장자명)가 ".py"인 경우
            print(full_filename)

search("C:/")
# C:\ 디렉토리에 파이썬 파일이 없다면 아무것도 출력되지 않는다.
# 이 파일들을 그대로 실행해 왔다면, 아무것도 출력되지 않을 것이다.
# 책을 그대로 따라왔다면, 많은 파일들이 검색될 것이다.
# 만약, 전자일 경우 파이썬 파일을 만들고 검색하거나,
# 디렉토리를 옮기면 제대로 작동하는 것을 볼 수 있을 것이다.