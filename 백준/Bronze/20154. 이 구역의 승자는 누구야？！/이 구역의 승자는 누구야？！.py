alpha  = [3,2,1,2,3,3,3,3,1,1,3,1,3,3,1,2,2,2,1,2,1,1,2,2,2,1]
s=input()
arr=[]
for a in s:
    i = ord(a) - ord('A')
    arr.append(alpha[i])

result = sum(arr) % 10
if result % 2:
    print("I'm a winner!")
else:
    print("You're the winner?")