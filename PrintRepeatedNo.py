a = int(input())
b = list(map(int, input().split()))
dup = []
for i in range(0, a):
    first = b[i]
    j = 0
    j = i+1
    while j < a:
        second = b[j]
        if first != second:
            j += 1
        elif first == second:
            dup.append(first)
            j = a+1
if len(dup) != 0:
    dup.sort()
    dup = {x for x in dup}
    for y in dup:
        print(y, end=" ")
else:
    print('unique')
