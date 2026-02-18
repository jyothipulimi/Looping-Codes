# To print Armstrong or Not

n = int(input("Enter n: "))     # 153
m = n                           # 153
rem = n
count = 0
sum = 0                         # 0
while rem > 0:
    count += 1                  # 1,2,3
    rem = rem//10               # 15,1,0
while m>0:
    d = m%10                    # 3, 5,1
    sum = sum+d**count          # 27,152,153
    m=m//10                     # 15,1,0
if sum == n:                    # 153 ==153 -- True
    print("Armstrong")          # Armstrong
else:
    print("Not Armstrong")