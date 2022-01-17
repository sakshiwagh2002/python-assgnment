# Enter number of terms needed                  
a=int(input("Enter the terms"))
f=0                                         
s=1                                         
if a<=0:
    print("The requested series is",f)
else:
    print(f,s,end=" ")
    for x in range(2,a+1):
        t=f+s                           
        print(t,end=" ")
        f=s
        s=t
