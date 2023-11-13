# Written by Jaymin Ding, Katia Ohmacht, and Xindi Liu from the Rye Country Day School

directions = list(map(int, input().split()))
m = list(map(int, input().split()))
fridge = []
for i in range(9):
    fridge.append(input())
fridge = [i.split("; ") for i in fridge]

x, y = 0, 0
steps = 0

for i in m:
    for j in range(i):
        a = steps + j
        dir = directions[a]
        if a % 2 == 0:
            x += dir
        else:
            y -= dir
    steps += i
    print(fridge[y % 9][x % 9])