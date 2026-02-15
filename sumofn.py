# sum of first 'n' Natural Numbers

n = int(input("Enter n: "))     # 5
sum = 0                         # 0
for i in range(1, n+1):         # 1,2,3,4,5
    sum = sum + i               # 1,3,6,10,15
print(sum)                      # 15