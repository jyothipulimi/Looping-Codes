# Odd Numbers

n = int(input("Enter n: "))     # 5
sum = 0                         # 0
for i in range(1, n+1):         # 1,2,3,4,5
    if i%2!=0:
        print(i)                # 1,3,5