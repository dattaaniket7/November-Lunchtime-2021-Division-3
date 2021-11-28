#Problem Code:CSTOCK
for i in range(int(input())):
    s,a,b,c=map(int,input().split())
    c=s+s*(c/100)
    if c>=a and c<=b:
        print("YES")
    else:
        print("NO") 
        
