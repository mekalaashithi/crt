#2)Accessing of list:
a=[10,20,30,40,50]
print(a[0])
print(a[-1])

#3) Creating List with repeated Elements
a=[10,20,30,40,50]
print(a *2)

#4) Adding Elements to List
a=[10,20,30,40,50]
a.append(100)
a.insert(1,50)
print(a)

#5) Removing Elements from List
a=[10,20,30,40,50]
a.remove(40)
print(a)
a.pop()
print(a)

#6) Slicing of List
a=[10,20,30,40,50]
print(a[0:])
print(a[2:])


#7) reverse the list using Slicing
a=[10,20,30,40,50]
print(a[::-1])
