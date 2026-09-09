for x in 'rakesh':
    print(x, end=' ')  
print()
for x in range(2, 7):
    print(x, end=' ')  
print()
for x in [1,2,3]:
    print(x, end=' ')
print()
for x in (4,5,6):
    print(x, end=' ') 
print()
for x in {7, 8, 9}:
    print(x, end=' ') 
print()
d = {1:'a', 2:'b', 3:'c'}
for x in d:
    print(x, end=' ')  
print()
for x in d.keys():
    print(x, end=' ')  
print()
for x in d:
    print(d[x], end=' ') 
print()
for x in d.values():   
    print(x, end=' ')
print()
for x in d.items():     
    print(x, end=' ')
print()
#index based for loop. 
l = [5,4,3,2,1]
#iterate from left to right 
for i in range(len(l)):
    print(l[i], end=' ')
print()
#iterate from right to left 
for i in range(len(l)-1, -1, -1):
    print(l[i], end=' ')
print()
#iterate from 3rd element 
for i in range(2, len(l)):
    print(l[i], end=' ')
print()
#iterate in steps of 2
for i in range(0, len(l), 2):
    print(l[i], end=' ')
print()

#tricky
l = [1, 2, 3, 4, 5, 6]
for x in l:
    print(x)
    l.remove(x)

#Homework
t = (5,4,3,2,1)
s = {5,4,3,2,1}
d = {5:'e', 4:'d', 3:'c', 2:'b', 1:'a'}
w = 'rakesh'
r = range(5,0,-1)
print()

#continue 
for x in range(1,11):
    if x % 3 == 0:
        continue 
    print(x,end=' ')    
print()
#break
for x in range(1,11):
    if x % 3 == 0:      
        break 
    print(x,end=' ')  
print()
#pass 
for x in range(1,11):
    pass
a = 21
#else 
for x in range(1,11):
    if x % 3 == 0:
        continue 
    print(x, end=' ')
else:
    print('Loop completed successfully')
print() 
for x in range(1, 11):
    if x % 3 == 0:
        break 
    print(x, end=' ')
else:
    print('Loop completed successfully') 
print('\n')
#assert
n = 10 
assert n > 5, 'N is not greater than 5' 
print('A')
assert n < 5, 'N is not lesser than 5' 
print('B')



