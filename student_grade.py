# student mark in 5 subjects (each out of 100)

sub1 = 78
sub2 = 85
sub3 = 92
sub4 = 74
sub5 = 88

# calculate total 
total = sub1 + sub2 + sub3 + sub4 + sub5 
percentage = total / 5

print("total",total,"/500")
print("percentage" and percentage, "%")

if  percentage >= 90 and percentage <= 100:
    print("grade = A+")
elif percentage >= 80 and percentage < 89:
    print("grade = A")
elif percentage >= 70 and percentage < 79:
    print("grade = B")
elif percentage >= 60 and percentage < 69:
    print("grade = C")
elif percentage >= 50 and percentage < 59:
    print("grade = D")
elif percentage < 50:
    print("grade = F")
else:    
    print("not found")