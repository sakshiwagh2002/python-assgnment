#write python program find armstrong number in an interval
a = int(input("Enter lower range: "))  
b = int(input("Enter upper range: "))  
  
for num in range(a,b + 1):  
   sum = 0  
   temp = num  
   while temp > 0:  
       digit = temp % 10  
       sum =sum+(digit*digit*digit)  
       temp =temp// 10  
       if num == sum:  
            print(num)  
