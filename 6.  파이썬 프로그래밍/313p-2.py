def get_total_page(m, n):
    if m%n == 0: # 문제가 된 상황을 따로 다루기 위해 조건문 사용
        return m//n
    else:
        return m//n + 1
    
print(get_total_page(5, 10))
print(get_total_page(15, 10))
print(get_total_page(25, 10))
print(get_total_page(30, 10)) # 정상적으로 3이 출력된다.