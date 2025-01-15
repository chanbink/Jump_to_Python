# os 라이브러리를 이용하면 324p.py와 같은 기능을 하는 코드를 만들 수 있다.

import os

for (path, dir, files) in os.walk("C:/"): # os.walk(): 디렉토리를 입력받아, 하위 디렉토리를 차례로(재귀적으로) 방문
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s%s" %(path, filename))

# os.path()는 반복문에서 한 번에 하나씩 탐색 결과를 튜플로 반환한다.