counter = input()
for i in range(0,counter,1):
    size = input()
    cubes = raw_input().split()
    start = 0
    end = len(cubes)-1
    last_used = None
    if(int(cubes[start])>int(cubes[end])):
        last_used=int(cubes[start])
        start = start + 1
    else:
        last_used=int(cubes[end])
        end = end - 1

    while(start<=end):
        if((int(cubes[start])>int(cubes[end])) and (int(cubes[start])<=last_used)):
            last_used=int(cubes[start])
            start = start + 1
        elif((int(cubes[start])<=int(cubes[end])) and (int(cubes[end])<=last_used)):
            last_used=int(cubes[end])
            end = end - 1
        else:
            break
    if start>end:
            print("Yes")
    else:
        print("No")