# 하위 디렉토리까지 모두 탐색하도록 코드를 수정하자.

import os

def search(dirname):
    try: # 접근 권한이 없는 디렉토리에 접근하면 PermissionError가 발생하므로 예외 처리
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename): # os.path.isdir(): 입력받은 대상이 디렉토리일 때 True 반환.
                search(full_filename) # 하위 디렉토리를 마주할 경우, 함수를 재호출
# 함수 내에서 함수를 다시 호출하도록 생성하는 것을 재귀 호출(recursive call)이라 한다.
            else: # 입력받은 대상이 디렉토리가 아닌 경우
                ext = os.path.splitext(full_filename)[-1]
                if ext == ".py":
                    print(full_filename)
    except PermissionError: # 접근 권한이 없는 디렉토리에 접근하여 PermissionError가 발생할 경우, 그냥 넘어감
        pass

search("C:/")