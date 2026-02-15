# Factorial Program

n = int(input("Enter n: "))     # 6
fact = 1
for i in range(1, n+1):         # 1,2,3,4,5,6
    fact = fact*i               # 1,2,6,24,120,720
print(fact)                     # 720