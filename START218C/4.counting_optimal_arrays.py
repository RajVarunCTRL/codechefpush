# cook your dish here
mod = 998244353
for _ in range(int(input())): # T inputs
    n,m = map(int,input().split())
    
    if n==1:
        print((m+1)%mod)
        continue
    if m==0:
        print(1)
        break
    
    temp = m.bit_length()
    max_xor = ( 1 << temp ) - 1
    res = (m - (max_xor-m) + 1)
    print(max(0,res)%mod)