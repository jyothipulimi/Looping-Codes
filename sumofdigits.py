# Sum of Digits

n = int(input("Enter n: "))     # 4321
sum=0                           # 0
for i in range(n):              # 4321,432,43,4
        sum = sum+n%10          # 1,3,6,10
        n=n//10                 # 432,43,4,0
print(sum)                      # 10