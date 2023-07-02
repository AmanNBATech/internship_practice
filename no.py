ph=float (input("enter number of physics")) 
m=float (input("enter number of maths")) 
b=float (input("enter number of biology")) 
ch=float (input("enter number of chemistry")) 
py=float (input("enter number of pyhton")) 
if (ph>33 and m>33 and b>33 and ch>33 and py>33):
  add=(ph+m+b+ch+py)
  print('total marks of student:=',add)
  average=(add/500)*100
  print('percentage of student:=',average)
  print('pass')
else:
 print('fail')   
