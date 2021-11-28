#Problem Code:EXPWEI
for i in range(int(input())):
    n=int(input())
    p=1
    mod=998244353
    if n%2==0:
        if n%4==0:
            q=1
            p=n//4
            p=p%mod
            p=p*(n+1)
            p=p%mod
            p=p*(n+1)
            p=p%mod
        else:
            q=2
            p=n//2
            p=p%mod
            p=p*(n+1)
            p=p%mod
            p=p*(n+1)
            p=p%mod
    else:
        q=1
        p=p*(n+1)//2
        p=p%mod
        p=p*(n+1)//2
        p=p%mod
        p=p*n
        p=p%mod
    inv=0
    if q==1:
        inv=1
    elif q == 2:
        inv=499122477
    ans=p*inv
    ans=ans%mod
    print(ans)
            