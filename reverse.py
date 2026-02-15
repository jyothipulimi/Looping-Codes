n = int(input("Enter n: "))     # 1223
rev = 0                         # 0
while n>0:                      # 1223 > 0
    d=n%10                      # 3,2,2,1
    rev = rev*10+d              # 3,32,322,3221
    n=n//10                     # 122,12,1,0
print("Reverse:", rev)          # 3221