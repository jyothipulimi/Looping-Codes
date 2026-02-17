# To Print Fibonacci sequence

n = int(input("Enter n: "))     # 5
a = 0
b = 1
c = 0
for i in range(c,n):            # 0,1,2,3,4,5
    print(a,end=" ")            # 0 1 1 2 3
    d=a+b
    a=b
    b=d
    c=c+1