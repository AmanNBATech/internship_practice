quiz1=[{1:'what is the capital of himmachal pradesh?','a':'shimla','b':'mandi','c':'kullu','d':'kangra'},'a']
quiz2=[{2:'how many states in the himachal pradesh?','a':'10','b':'9','c':'12','d':'14'},'c',]
      
print(quiz1[0][1])
print(quiz1[0]['a'])
print(quiz1[0]['b'])
print(quiz1[0]['c'])
print(quiz1[0]['d'])

ans=input('enter any number in 1 to 4')
if ans ==quiz1[1]:
    print('right')
else:print('wrong')  

print(quiz2[0][2])
print(quiz2[0]['a'])
print(quiz2[0]['b'])
print(quiz2[0]['c'])
print(quiz2[0]['d'])

ans=input('enter any number in 1 to 4')
if ans ==quiz2[1]:
    print('right')
else:print('wrong')    