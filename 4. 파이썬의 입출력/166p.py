def say_myself(name, man=True, age): # 오류: 디폴트로 초기화된 변수는 그렇지 않은 변수보다 항상 뒤에 두어야 한다.
    print("My name is %s." %name)
    print("I'm %d years old." %age)
    if man:
        print("I'm male.")
    else:
        print("I'm female.")

say_myself('Chanbin Koo', 27) # 만약 위의 함수를 오류로 두지 않을 경우, 인터프리터가 27을 어디로 전달할 지 판단할 수 없다.