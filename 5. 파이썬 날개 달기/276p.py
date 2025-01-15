import zipfile

# zipfile.ZipFile()은 .zip 파일 관리를 위한 객체를 생성한다.
with zipfile.ZipFile('unnie.zip', 'w') as myzip: # unnie.zip 파일을 만들기 위한 {myzip} 객체 생성
    myzip.write('miyeon.txt') # write(): {myzip} 객체에 파일을 추가
    myzip.write('minnie.txt')
    myzip.write('soyeon.txt')


with zipfile.ZipFile('unnie.zip') as myzip:
    myzip.extractall() # extractall(): 모든 파일을 해제하여 개별 파일로 분리