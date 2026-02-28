'''li=[1,2,3,4,5]
res = []
for i in li:
    res.append(i** 2)
print(res)

ans = [i**2 for i in li]
print(ans)'''
'''1.pyramid
n = 4
Output:
        *
      *   *
    *   *   *
  *   *   *   *  

  '''
n = int(input())
for i in range(1,n+1):
    print(" " * (n-i) + "* " * i)
print("------------------------------")
for i in range(n,0,-1):
    print(" " *(n-i)+"* " *i) 
print("-------------------------------")
n = int(input())
for i in range(1,n+1):
    print(" " * (n-i)+"1 " * i)