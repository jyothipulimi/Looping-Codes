# To Print Even Number Or odd

n=int(input("Enter n: "))           # 10
e=int(input("Enter n: "))           # 20
sum = 0                             # 0
for i in range(n,e+1):              # 10,11,12,13,14,15,16,17,18,19,20
    if i%2==0:
        print(i,"is Even Number")   # 10,12,14,16,18,20
    else:
        print(i,"is Odd number")    # 11,13,15,17,19