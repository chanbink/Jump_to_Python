try:
    a = [1, 2]
    print(a[3]) # IndexError가 발생하여 except 블록으로 바로 이동
    4 / 0 # ZeroDivisionError는 발생하지 않는다.

except ZeroDivisionError:
    print("You can't divide a number by 0.")

except IndexError:
    print("Your index is out of range.")