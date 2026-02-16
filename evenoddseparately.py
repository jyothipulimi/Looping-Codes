# Write code to find the sum of all even numbers and odd numbers separately.

even_list = []
odd_list = []
for i in range(1, 101):
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
print("Even numbers:", even_list)
print("Odd numbers:", odd_list)
