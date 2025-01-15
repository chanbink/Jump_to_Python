import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace('\t', ' '*4)

f = open(dst, 'w') # 바꾼 내용을 파일로 만들어 출력
f.write(space_content)
f.close()