#write a string which contain vowels.

str=input("Enter the String:")
list=['a','e','i','o','u','A','E','I','O','U']
for i in list:
    if i not in str:
        print("string not contains vowels:")
        break
    else:
        print("String contain vowels:")
        break


#output:
Enter the String:Ganesh jore tybcs
String contain vowels:
