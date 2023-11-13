def charSorting(unordered):
    alp = "abcdefghijklmnopqrstuvwxyz"
    cnt = [0 for i in range(26)]
    for i in list(unordered):
        cnt[alp.index(i)] += 1

    for i in range(len(cnt)):
        cnt[i] = [cnt[i], alp[i]]

    cnt = sorted(cnt, key=lambda x: x[0], reverse=True)
    cnt = [i[1]*i[0] for i in cnt]

    return "".join(cnt)

a = input()
b = input()
print(charSorting(b))