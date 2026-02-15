# Palindrome
"""
n = int(input("Enter n: "))     # 121                   # 1223
m = n                           # m=121                 # 1223
s = 0                           # 0                     # 0
while n>0:                      # 121 > 0 -- True       # 1223 > 0
    d=n%10                      # 1,2,1                 # 3,2,2,1
    s=s*10+d                    # 1,12,121              # 3,32,322,3221
    n=n//10                     # 12,1,0                # 122,12,1,0
if s==m:                        # 121 == 121 -- True    # 3221 == 1223 -- False
    print("Palindrome")         # Palindrome
else:
    print("Not a Palindrome")                           # Not a Palindrome

"""

n = input("Enter n: ")          # madam
rev = ""                        # "" -- Empty String
for i in n:                     # m,a,d,a,m
    rev = i + rev               # 'm','am','dam','adam','madam'
if rev == n:                    # madam == madam -- True
    print("Palindrome")         # Palindrome
else:
    print("Not a Palindrome")
