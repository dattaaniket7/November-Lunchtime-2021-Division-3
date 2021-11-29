#Problem Code:RPDRDNG 
t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int, input().split()))
    s = list(set(li))
    s.sort()
    f = []
    for j in range(len(s)):
        me = j//2
        f.append(s[me])
    g = len(s)
    for j in range(len(s)):
        me = (j+g-1)//2
        f.append(s[me])
    f.sort()
    li.sort()
    if f==li:
        print(" ".join(map(str, s)))
    else:
        print(-1)