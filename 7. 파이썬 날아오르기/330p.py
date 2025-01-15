# 1. EUC-KR로 작성된 파일 읽기
with open("euc_kr.txt", encoding='euc-kr') as f: # 작성된 파일이 EUC-KR로 인코딩됨을 알려줌
    data = f.read() # 읽은 문자열은 유니코드 문자열로 저장된다.

# 2. 유니코드 문자열로 프로그램 수행하기
data = data + '\n' + '문자열 추가' # 추가되는 문자열은 당연히 유니코드 문자열이다.

# 3. EUC-KR로 수정된 문자열 저장하기
with open("euc_kr.txt", encoding='euc-kr', mode='w') as f:
    f.write(data) # 유니코드 문자열이 EUC-KR로 인코딩되어 적힌다.