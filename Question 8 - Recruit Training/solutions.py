answer = None

n = input()
chef_one_ban = input().split(" ")
chef_two_ban = input().split(" ")
chef_three_ban = input().split(" ")

# the above three lists are guaranteed to have same len, so we can iterate the following to "transpose" the structure

all_bans_by_day = []

for i in range(len(chef_one_ban)):
    all_bans_by_day.append([chef_one_ban[i], chef_two_ban[i], chef_three_ban[i]])

combinations_by_day = []

for day in all_bans_by_day:
    if len(set(day)) <= 1:
        answer = 0
        print(answer)
        exit()
    else:
        combinations_by_day.append(2)

answer = 1
modnum = 10**9 + 7

for i in combinations_by_day:
    answer = (answer * i) % modnum

print(answer)