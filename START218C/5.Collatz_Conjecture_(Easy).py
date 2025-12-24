# cook your dish here

# TLE, but works for small inputs ig.
    # Hmmm
    # https://www.codechef.com/viewsolution/1221123261
    
for _ in range(int(input())): # T inputs
    n = int(input())
    
    vis = {n}    # seen numbers
    q = [n]      # queue
    boo = False
    
    while q:
        curr=q.pop(0)
        
        if curr==1:
            boo = True
            break
        xor_next = (3^curr) + 1
        if xor_next not in vis:
            vis.add(xor_next)
            q.append(xor_next)
            
        if curr%2==0:
            nh = curr//2
            if nh not in vis:
                vis.add(nh)
                q.append(nh)
    if boo:
        print("Yes")
    else:
        print("No")