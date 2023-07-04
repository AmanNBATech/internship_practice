import random

a=random.randint(1,10)
b=int(input("enter any number"))
print(b)
print(a)
if a==b:
    print("number is same")
elif a>b:
    print("first number is larger")
elif a<10:
    print("you cant number larger then 10")

else:
    print("you cant add -1")
    