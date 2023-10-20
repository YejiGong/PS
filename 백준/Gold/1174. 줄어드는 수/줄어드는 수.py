from itertools import combinations

N=int(input())
nums=[]
for i in range(1,11):
    for comb in combinations(range(0,10),i):
        comb = list(comb)
        comb.sort(reverse=True)
        nums.append(int("".join(map(str,comb))))
nums.sort()
try:
    print(nums[N-1])
except:
    print(-1)