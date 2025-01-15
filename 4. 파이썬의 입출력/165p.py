def say_myself(name, age, man=True): # 함수를 정의할 때 매개변수에 값을 대입하면 디폴트로 설정된다.
    print("My name is %s." %name)
    print("I'm %d years old." %age)
    if man:
        print("I'm male.")
    else:
        print("I'm female.")

say_myself("Chanbin Koo", 27) # {man}에 입력값을 주지 않았으나, 자동으로 True가 된다. 
say_myself("Chanbin Koo", 27, True) # {man}에 인수 True가 전달된다. 위와 같은 결과가 출력된다.

say_myself('Nicha Yontararak', 29, False) # {man}에 인수 True가 전달되어 else 블록이 실행된다.