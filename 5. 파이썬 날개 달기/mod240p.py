class MyError(Exception):
    def __str__(self): # __str__(): 오류 메시지를 반환하여 오류 변수에 전달할 때 사용하는 Exception 클래스의 메서드
        return "You have been banned from chatting for 3 minutes."