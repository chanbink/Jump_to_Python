import re
p = re.compile('^python\s\w+') # ^: 문자열의 처음을 의미하는 메타 문자
# '^python\s\w+'는 python으로 시작, 화이트스페이스 다음에 문자가 와야 함을 의미하는 정규식이다.

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data)) # 문자열의 처음은 첫 줄이므로 'python one'민 매칭