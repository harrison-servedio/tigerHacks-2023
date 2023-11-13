# Written by Ajay Bagaria, Jack Whitney-Epstein, and Vikram Sarker from the Brunswick School

size = int(input())
startinput = input().split()
endinput = input().split()

arr = [[-1 for i in range(0, size)] for j in range(0, size)]

for i in range(0,2):
    startinput[i] = int(startinput[i]) - 1
    endinput[i] = int(endinput[i]) - 1
    
arr[startinput[0]][startinput[1]] = 0

if((startinput[0] == endinput[0]) and (startinput[1] == endinput[1])):
    print(0)
else:
    depth = 1
    while(arr[endinput[0]][endinput[1]] == -1):
        for i in range(size):
            for j in range(size):
                if arr[i][j] == depth-1:
                    #check if 8 moves are in and then if so assign them to depth
                    if((0 <= i+1 < size) and (0<= j+2 < size)):
                        if(arr[i+1][j+2] == -1):
                            arr[i+1][j+2] = depth
                    if((0 <= i+1 < size) and (0<= j-2 < size)):
                        if(arr[i+1][j-2] == -1):
                            arr[i+1][j-2] = depth
                    if((0 <= i-1 < size) and (0<= j+2 < size)):
                        if(arr[i-1][j+2] == -1):
                            arr[i-1][j+2] = depth
                    if((0 <= i-1 < size) and (0<= j-2 < size)):
                        if(arr[i-1][j-2] == -1):
                            arr[i-1][j-2] = depth
                    if((0 <= i+2 < size) and (0<= j+1 < size)):
                        if(arr[i+2][j+1] == -1):
                            arr[i+2][j+1] = depth
                    if((0 <= i+2 < size) and (0<= j-1 < size)):
                        if(arr[i+2][j-1] == -1):
                            arr[i+2][j-1] = depth
                    if((0 <= i-2 < size) and (0<= j+1 < size)):
                        if(arr[i-2][j+1] == -1):
                            arr[i-2][j+1] = depth
                    if((0 <= i-2 < size) and (0<= j-1 < size)):
                        if(arr[i-2][j-1] == -1):
                            arr[i-2][j-1] = depth
        depth += 1
    print(arr[endinput[0]][endinput[1]])