#write a python program to check no is prime or not
num=int(input("enter the number:"))
flag=0
for i in range(2,num):
     if(num%i==0):
            flag=1
     if(flag==0):
            print("no is prime:")
            break
else:  
            print("no is not prime:") 
