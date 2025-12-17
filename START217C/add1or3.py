# cook your dish here
for _ in range(int(input())):
    n,m = map(int,input().split())
    print("Yes" if ((n<=m<=3*n) and (m-n)%2==0) else "No")

        