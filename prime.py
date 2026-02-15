# Prime Number or Not

n = int(input("Enter n: "))     # 7
flag = 1                        # 1
for i in range(2,n):            # 2,3,4,5,6
    if n%i == 0:
        flag = 0
        break
if flag == 1:                   # 1 == 1 -- True
    print("Prime")              # Prime
else:
    print("Not a prime")