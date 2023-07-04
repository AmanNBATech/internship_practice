import random
level=int(input("enter any level you want to play"))
print(level)
if (level)==1:

 for i in range(1,4):
    
    
    
  if i==1:
      
      a=random.randint(1,4)
      b=int(input("play first chance "))
      print("this is your first chance") 
      if (a==b):
            print("you won")

            print(a,b)
            break
      else:
         print("you lose")
         print(a,b)
         
  if i==2:
        a=random.randint(1,19)
        b=int(input("play second chance "))
       
        if (a==b):
          print("you won")
          print(a,b)
          break
        else:
          print("you loose second time") 
          print(a,b)   
  if i==3:
        a=random.randint(1,19)
        b=int(input("play Third chance "))
        
        if (a==b):
         print("you won")
         print(a,b)
         break
        else:
         print("you loose third time")  
         print(a,b)

if level==2:
 a=random.randint(1,50)
 for i in range(1,4):
    
    
    
  if i==1:
      b=int(input("play first chance "))
      print("this is your first chance") 
      if (a==b):
         print("you won")

         print(a,b)
         break
      else:
         print("you lose")
         print(a,b)
         
  if i==2:
        a=random.randint(1,50)
        b=int(input("play second chance "))
       
        if (a==b):
          print("you won")
          print(a,b)
          break
        else:
          print("you loose second time") 
          print(a,b)   
  if i==3:
        a=random.randint(1,50)
        b=int(input("play Third chance "))
        
        if (a==b):
         print("you won")
         print(a,b)
         break
        else:
         print("you loose third time")  
         print(a,b)
if level==3:
     a=random.randint(1,100)
for i in range(1,4):
    
    
    
  if i==1:
      b=int(input("play first chance "))
      print("this is your first chance") 
      if (a==b):
            print("you won")

            print(a,b)
            break
      else:
         print("you lose")
         print(a,b)
         
  if i==2:
        a=random.randint(1,100)
        b=int(input("play second chance "))
       
        if (a==b):
          print("you won")
          print(a,b)
          break
        else:
          print("you loose second time") 
          print(a,b)   
  if i==3:
        a=random.randint(1,100)
        b=int(input("play Third chance "))
        
        if (a==b):
         print("you won")
         print(a,b)
         break
        else:
         print("you loose third time")  
         print(a,b)






    