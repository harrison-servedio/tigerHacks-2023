import math

a = float(input())
b = float(input())
c = [float(i) for i in input().split(",")]

d = 0

for i in c:
    d +=((i**2)/100 * 0.01 * a * 18)


print(math.ceil(d))