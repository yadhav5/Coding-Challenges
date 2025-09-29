
def armstrong(num):
    total = 0
    n_str = str(num)
    power = len(n_str)
    for i in n_str :
        dig_pow = int(i)**power
        total = total + dig_pow
    return total

n = int(input("Enter The Number:"))
if n == armstrong(n):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")  
        
        
