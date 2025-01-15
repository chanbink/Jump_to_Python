# 디렉토리의 파일과 디렉토리를 검색하도록 코드 변경

import os

def search(dirname):
    filenames = os.listdir(dirname) # os.listdir(): 입력받은 경로의 파일이나 디렉토리 이름을 리스트로 반환
    for filename in filenames:
        full_filename = os.path.join(dirname, filename) # os.path.join(): 반환된 파일 이름이 경로를 포함하도록 합침
        print(full_filename)

search("C:/") # C:\ 디렉토리의 모든 파일과 디렉토리를 검색