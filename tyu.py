import random

a=random.randint(1,7)
for i in range(1,4):
    
    
    
 if i==1:
      b=int(input("play first chance "))
      print("this is your first chance") 
      if (a==b):
            print("you won")

            print(a)
            break
      else:
         print("you lose")
         print(a)
         
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
         print(a)

      
    

print(b)





# import random

# fruits = ['apple', 'banana', 'orange', 'grape']

# random_fruit = random.choice(fruits)
# print(random_fruit)

# import random

# cards = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']

# random.shuffle(cards)
# print(cards)

    