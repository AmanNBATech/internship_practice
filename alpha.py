# for i in range(1,6):
#     for j in range(1,6):
#         if (i == 1 or i == 3 or i == 6 ) and (j<5) or j == 1 or j ==0 and(i == 2 or i == 3) :
#             print('* ',end='')
#         else:
#             print('  ',end='')
#     print()
    



# for i in range(1,6):
#     for j in range(1,6):
#         if (i == 1 or i == 3 or i == 5 ) and (j<5) or j == 1 or j ==0 and(i == 2 or i == 3) :
#             print('* ',end='')
#         else:
#             print('  ',end='')
#     print()
# for i in range(1,6):
#     for j in range(1,6):
#         if (i ==  1 or i == 5 ) and (j<6) or j == 3 or j ==0 and(i == 2 ) :
#             print('* ',end='')
#         else:
#             print('  ',end='')
#     print()
# for i in range(1,6):
#     for j in range(1,6):
#         if (i ==  1  ) and (j<6) or j == 3 or j ==0 and(i == 2 ) :
#             print('* ',end='')
#         else:
#             print('  ',end='')
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         if (i == 1 or i == 5 ) and (j<=3) or j == 1 or j ==4 and(i == 2 or i == 3 or i == 4) :
#             print('* ',end='')
#         else:
#             print('  ',end='')
#     print()
    
# for i in range(1,6):
#     for j in range(1,6):
#         if (i == 1 or i == 5 ) and (j>=3) or j == 2  and( i==2 or i==3 or i==4 ) :
#             print('* ',end='')
#         else:
#             print('  ',end='')
#     print()
    
# for i in range(1,6):
#     for j in range(1,6):
#         if (i == 5 ) and (j<6) or j == 1 or j ==0 and(i == 2 ) :
#             print('* ',end='')
#         else:
#             print('  ',end='')
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         if ( i==2 and j==2 or (i==3 and j==3)or(i==4 and j==4)) or j>4 or j==1   and(i==1 or i==2 or i==3 or i==4 or i==5 ) :
#             print('* ',end='')
#         else:
#             print('  ',end='')
#     print()

# for i in range(0,7):
#     for j in range(0,7):
#         if  j==0 or j==6 or ((i==j)and(j>0 and j<4)) or(i==1 and j==5) or (i==2 and j==4) :
#             print('* ',end='')
#         else:
#             print('  ',end='')
#     print()

# for i in range(1,7):
#     for j in range(1,7):
#         if ( (j==1 or j==5) and i!=6 or i==6 and j>1 and j<5):
#             print('* ',end='')
#         else:
#             print('  ',end='')
#     print()
for i in range(1,7):
    for j in range(1,7):
        if  (j==1 or j==5) and i!=1 and i!=6 or(( i==1 or i==6 )and (j>1 and j<5)):
            print('* ',end='')
        else:
            print('  ',end='')
    print()
# for i in range(1,6):
#     for j in range(1,6):
#         if i==j or i+j == 6  :
#             print('* ',end='')
#         else:
#             print('  ',end='')
#     print()
# for i in range(1,7):
#     for j in range(1,7):
#         if  ((i==0 or i==3 or i==6) and (j>0 and j<4))  or( j==0 and (i>0 and i<3)) or (j==4 and (i>3 and i<6)):
#             print('* ',end='')
#         else:
#             print('  ',end='')
#     print()