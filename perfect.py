# Perfect Number or not

n = int(input("Enter n: "))     # 6
m = 0                           # 0
for i in range(1,n):            # 1,2,3,4,5
    if n%i==0:
        m = m+i                 # 1,3,6
if m == n:                      # 6 == 6 -- True
    print("Perfect Number")     # Perfect NUmber
else:
    print("Not a Perfect Number")