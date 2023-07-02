
print ("Please select the operation.")    
print ("a: Add")    
print ("b: Subtract")    
print ("c: Multiply")    
print ("d: Divide")    
def add(a, b):    
   return a + b   
def subtract(a, b):   
   return a - b   
def multiply(a, b):   
   return a * b   
def divide(a, b):  
 
   return a / b   
def modulo(a,b):


   return(a%b) 

enter = input("Please enter choice (a/ b/ c/ d): ")    
    
num_1 = int (input ("Please enter the first number: "))    
num_2 = int (input ("Please enter the second number: "))    
    
if enter == 'a':    
   print (num_1, " + ", num_2, " = ", add(num_1, num_2))    
    
elif enter == 'b':    
   print (num_1, " - ", num_2, " = ", subtract(num_1, num_2))    
    
elif enter == 'c':    
   print (num_1, " * ", num_2, " = ", multiply(num_1, num_2))    
elif enter == 'd':    
   print (num_1, " / ", num_2, " = ", divide(num_1, num_2))   
elif enter == 't':
   print(num_1,"%",num_2,"=",modulo(num_1,num_2)) 
else:    
   print ("wrong input")    