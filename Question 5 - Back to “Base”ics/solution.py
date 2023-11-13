digs = list("0123456789ABCDEF")


def convertToBase(num, base):
    if num < base:
        return digs[num]
    return convertToBase(num//base, base) + digs[num%base]


def conv(start, end, num):
    
    x = convertToBase(int(str(num), start), end)
    return sum([digs.index(i) for i in list(x)])

a = int(input())
b = int(input())
c = str(input())

print(conv(a, b, c))