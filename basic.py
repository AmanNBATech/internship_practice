myList = [1, 2, 3, 'EduCBA', 'makes learning fun!']
myList.append(4)
myList.append(5)
myList.append(6)
for i in range(7,8):
    myList.append(i)
print(myList)
this = [1,2,3,4,5,6,7]
for i in range(8,11):
    this.append(i)
print(this)
that = [1,2,3,45,6,]
that.extend([8,9,0,7,])
that.insert(2,9)
print(that)
what = [2,3,4,5,6,7,8,7,7,23]
what.reverse()
print(len(what))
print(min(what))
print(what.count(7))
print(this+what)
print(this*3)
print(what.index(3))
what.sort()
print(what)

what.clear()
print(what)
bit=[23,4,5,3,53,53,24,3]
print(bit[:4])
print(bit[2:])
print(bit[1:4])
print(bit[::-1])
bit.pop(4)







