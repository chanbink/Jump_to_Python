try:
    age = int(input("Enter your age: ")) # 숫자를 입력받아 정수로 변환

except:
    print("Your input is incorrect.") # 오류가 발생할 경우 except 블록 실행

else: # 오류가 발생하지 않을 경우, else 블록 실행
    if age <= 18:
        print("Minors are prohibited from entering.")
    else:
        print("Welcome!")