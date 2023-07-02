# n=int(input("enter any number"))
# for i in range(n):
#     for j in range(i+1):
#       print(" ",end='')
#     for j in range(i,n):
#        print('*',end='')
#     print()
        
# n=int(input("enter any number"))
# for i in range(n):
#     for j in range(i,n):
#       print(" ",end='')
#     for j in range(i+1):
#        print('*',end='')
#     print()
        

# n=int(input("enter any number"))
# for i in range(n):
#     for j in range(i,n):
#       print("*",end='')
#     print()


# n=int(input("enter any number"))
# for i in range(n):
#     for j in range(i+1):
#       print("*",end='')
#     print()
    

# n=int(input("enter any number"))
# for i in range(n,0,-1):
#     for j in range(0,n-i):
#       print(end=" ")
#     for j in range(0,i):
#       print('*',end=" ")
#     print()
    
            
# for i in range(1,6):
#     for j in range(1,6):
#         if i == 1 or j == 1 or i == 5 or j == 5:
#             print('* ',end='')
#         else:
#             print('  ',end='')
#     print()

            
# for i in range(1,6):
#     for j in range(1,6):
#         if (i == 3) and (j<5) or j == 1 or j ==4  and(i == 1 or i==2 or i==4 or i == 5 ) :
#             print('* ',end='')
#         else:
#             print('  ',end='')
#     print()
for i in range(1,6):
    for j in range(1,6):
        if (i == 3) and (j<5) or j == 1 or j ==4  and(i == 1 or i==2 or i==4 or i == 5 ) :
            print('* ',end='')
        else:
            print('  ',end='')
    print()