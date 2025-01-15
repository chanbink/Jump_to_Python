# 문제: 가진 돈의 2/5로 학용품을 샀다. 쓴 돈이 1760원일 때 남은 돈은?
from fractions import Fraction
import sympy

#미지수 정의
x = sympy.symbols('x')

# 방정식 정의
f = sympy.Eq(x*Fraction('2/5'), 1760)

# 방정식 풀이
result = sympy.solve(f)

# 남은 돈 구하기
remains = result[0] - 1760

print("Remains are {} won.".format(remains))