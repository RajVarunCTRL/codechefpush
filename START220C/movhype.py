# cook your dish here
for _ in range(int(input())): #T inputs
    n = int(input()) # 2n+1
    # totalSeats = (2*n)+1
    lst = list(map(int,input().split())) # hype levels of people in seats 1,3,5 (2n+1)
    
    # all even numbered seats are empty
    # all odd numbered seats are full ig
    # for each i 1,2,3,n+1
    # so even numbered seats hype is max of left and right seat 2 = max(seat1 and seat2)
    loudnesslevels = []
    
    for i in range(n):
        loudness = max(lst[i],lst[i+1])
        loudnesslevels.append(loudness)
    print(min(loudnesslevels))
    
    