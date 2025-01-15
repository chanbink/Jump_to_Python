import sys # import: 모듈, 라이브러리, 파일 등 외부 요소들을 도입하는 예약어.

args = sys.argv[1:] # {argv}: 프로그램 실행 시에 전달받은 인수를 요소로 하는 리스트
for i in args:
    print(i) # {argv}의 첫 번째 요소는 파일 이름이다. 따라서, 이 파일의 {argv[0]}는 '183p.py'이다.

# 파이썬 파일을 실행할 때, python 183p.py aaa bbb ccc의 명령어를 실행하면
# 183p.py 내의 리스트 {argv}에 'aaa', 'bbb', 'ccc'가 전달되어 다음과 같다.
# sys.argv == ['183p.py', 'aaa', 'bbb', 'ccc']