#write a python program to print all prime no in an interval:
a=int(input("enter the starting interval:"))
b=int(input("enter the ending interval:"))
for n in range(a,b):
     flag=0
for i in range(2,n):
            if(n%i==0):
                 flag=1
                 break
            if(flag==0):
                 print(n)
