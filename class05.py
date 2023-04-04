# if statement
a = input()
b = input()
if a>b:
    print(" a is greater than b")
else:
    print (" b is grater than a")

# nested if
num = int(input())
if(num>0):
    if(num==0):
        print("zero")
    else:
        print("positive number")
else:
    print ("negative number")

# elif statement
score = int(input())
if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print(" fail ")

# short hand
a = int(input())
b = int(input())
print("b is big") if b>a else print ("a is big")

# short hand
a = int(input())
result = "positive" if a>0 else "negative"
print (result)

# logical oparator
age = 18
flower = True
if age>18 or  flower==True:
    print("you can marry me")
else:
    print("you can't marry me")