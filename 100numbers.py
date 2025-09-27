num = []
even = []
odd = []
divisible_by_5_and_3 = []

for i in range(1, 101):
    num.append(i)
print(num)


for i in num:
    if i % 2 == 0:
       even.append(i) 
else:
       odd.append(i)


print("Even Number:", even)
print("Odd Number:", odd)     


for i in(num):
    if i % 5 == 0 and i % 3 == 0:
        divisible_by_5_and_3.append(i)


print("Numbers Divisible By Both 5 and 3:", divisible_by_5_and_3)