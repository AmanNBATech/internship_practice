# ph=float (input("enter number of physics")) 
# m=float (input("enter number of maths")) 
# b=float (input("enter number of biology")) 
# ch=float (input("enter number of chemistry")) 
# py=float (input("enter number of pyhton")) 
# if (ph>33 and m>33 and b>33 and ch>33 and py>33):
#   add=(ph+m+b+ch+py)
#   print('total marks of student:=',add)
#   average=(add/500)*100
#   print('percentage of student:=',average)
#   print('pass')
# else:
#  print('fail')   


# class Abc:
#     def home(self,a):
#         print("i am Home",a)

#     def home1(self,a):
#         print("i am Home",a)

# a = Abc()
# a.home(2)
# b=Abc()
# b.home1(5)

# class Abc:
#     def __init__(self,a,b):
#         # print("hello",a+b)
#         self.a = a
#         self.b = b

#     def add(self):
#         print(self.a+self.b)

#     def divide(self):
#       print(self.a/self.b)

# a = Abc(4,5)
# a.add()
# a.divide()


class abc:
    def __init__(self) -> None:
        print("i am parent")
    
class b(abc):
    def __init__(self) -> None:
        super().__init__()
        print("i am hello")

class h(b):
    def __init__(self) -> None:
        super().__init__()
        print("i am aman")

d = h()