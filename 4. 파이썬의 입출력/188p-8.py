import sys

args = sys.argv[1:]
sigma = 0
for i in args:
    sigma += int(i)

print(sigma)