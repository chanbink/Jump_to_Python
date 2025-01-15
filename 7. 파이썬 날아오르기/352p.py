def add(a: int, b: int) -> int:
    return a + b

result = add(3, 3.4) # int라 명시한 {b} 매개변수에 float인 3.4가 전달된다.
print(result) # int를 반환한다고  명시된 add() 역시 float인 {result}를 반환한다.

# 타입 어노테이션에 강제성은 없음을 알 수 있다.