# cook your dish here
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    tc = sum((i+1) * lst[i] for i in range(n))
    print(tc)