a = int(input())
b = int(input())
c = int(input())
d = input()

def fibGen(start1, start2, depth):
    if depth == 1: return start1
    elif depth == 2: return start2
    else: return fibGen(start2, start1+start2, depth-1)

def decode(message, fibNum1, fibNum2, numCount):
    map = {}
    output = []
    nums = message.split(" ")
    for i in range(numCount):
        num = nums[i]
        if not num in map:
            map[str(num)] = chr(int(str(fibGen(int(fibNum1), int(fibNum2), int(num)))[-2:]))
        output.append(map[str(num)])

    return "".join(output)


print(decode(d, a, b, c))