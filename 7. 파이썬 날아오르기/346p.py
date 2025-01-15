def mygen():
    for i in range(1, 1000):
        result = i * i
        yield result # yield문이 999개 있는 것과 같다.

gen = mygen()

print(next(gen))
print(next(gen))
print(next(gen))