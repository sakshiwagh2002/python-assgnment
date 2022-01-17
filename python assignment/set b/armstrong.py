#write a python program to check no is armstrong or not
num=int(input("enter  the number:"))
sum = 0

num1 = num
while num1 > 0:
   digit = num1 % 10
   sum =sum+(digit*digit*digit)
   num1 =num1//10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

