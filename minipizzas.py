def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
for i in range (int(input())):
    n,k=map(int,input().split())
    p=0
    g=gcd(n,k)
    p=n//g
    print(p)