# To Print Fibonacci sequence

n = int(input("Enter n: "))     # 5
a = 0
b = 1
c = 0
for i in range(0,n):            # 0,1,2,3,4,5
    print(a,end=" ")            # Output - 0 1 1 2 3
    d=a+b                       # 1,2,3,5,8
    a=b                         # 1,1,2,3,5
    b=d                         # 1,2,3,5,8
    c=c+1                       # 1,2,3,4,5