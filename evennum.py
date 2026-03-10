# To print Even Numbers

n = int(input("Enter n: "))     # 15
for i in range(1,n+1):          # 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
    if i%2 == 0:                # 2,4,6,8,10,12,14 -- True
        print(i)                # 2,4,6,8,10,12,14
