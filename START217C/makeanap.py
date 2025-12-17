# cook your dish here
import math
def temp(lst_nums):
    res = lst_nums[0]
    for i in lst_nums[1:]:
        res = math.gcd(res,i)
    return res

for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    differences = []
    for i in range(n-1):
        differences.append(lst[i+1] - lst[i])
    common_in_differences = temp(differences)
    min_operations = (lst[-1]-lst[0])//common_in_differences+1
    print(min_operations-n)