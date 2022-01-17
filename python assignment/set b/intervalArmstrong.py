#write a python program find armstrong number in an interval time:
a=int(input("starting number:"))
b=int(input("ending number:"))
for i in renge(a,b):
      n=i
      s=0
while(n>0):
 d=n%10
 n-int(n%10)
 s=s+(d*d*d)
if(s==i):
                print(i)
