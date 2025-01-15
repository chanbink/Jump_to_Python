import re
p = re.compile('^python\s\w+', re.MULTILINE) # re.MULTILINE에 의해 메타 문자 ^가 각 줄의 처음으로 의미가 변경

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data)) # 'python + 화이트스페이스 + 단어' 형태의 모든 부분이 반환된다.