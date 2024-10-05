n = int(input("Enter 3 digit number:"))
add = 0
temp = n
while temp >0:
    digit = temp % 10 
    add += digit **3
    temp //=10
if n == add:
  print("Armstong number")
else:
   print("Not an armstrong number")