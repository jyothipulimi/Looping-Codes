# Sum of Squares

n = int(input("Enter n: "))     # 4
sum = 0                         # 0
for i in range(1, n+1):         # 1,2,3,4
    sum = sum+i*i               # 1,5,14,30
print(sum)                      # 30