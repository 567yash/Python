# # Set Methods 
# #add 
# s = set()
# s.add(1)
# s.add(1.6)
# s.add(2+3j)
# s.add(True)
# s.add(None)
# # s.add([1,2,3])
# s.add((4,5,6))
# # s.add({7,8,9})
# # s.add({10:'a', 11:'b', 12:'c'})
# s.add('rakesh')
# s.add(range(13,16))
# print(s)

# #update
# s = set()
# # s.update(1)
# # s.update(1.6)
# # s.update(2+3j)
# # s.update(True)
# # s.update(None)
# s.update([1,2,3])
# s.update((4,5,6))
# s.update({7,8,9})
# s.update({10:'a', 11:'b', 12:'c'})
# s.update('rakesh')
# s.update(range(13,16))
# print(s)

# #pop
# s = {1,4,3,2,5,6,7,9}
# print(s)   
# a = s.pop()    # 1{4,3,2,5,6,7,9}
# print(a, s)
# b = s.pop()   # 4 {3,2,5,6,7,9}
# print(b, s)
# c = s.pop(3)  # TypeError: set.pop() takes no arguments (1 given)
# print(c, s)

# #remove
# s = {4,3,2,5,8}
# a = s.remove(8) 
# print(a, s) #output: None {2, 3, 4, 5}
# b = s.remove(9)  #error: KeyError: 9
# print(b, s)

# # discard
# s = {4,3,2,5,8}
# a = s.discard(8) #output: None {2, 3, 4, 5}
# print(a, s)
# b = s.discard(9)  #none{2, 3, 4, 5}
# print(b, s)

# # clear
# s = {4,3,5,2,1}
# a = s.clear() #all elements removed, output: None set()
# print(a, s)

# # union, intersection, differece, symmetric_difference
# s = {1,2,3,4}
# l = [3,4,5,6]
# t = (3,4,5,6)
# s2 = {3,4,5,6}
# d = {3:'c', 4:'d', 5:'e', 6:'f'}
# r = range(3,7)
# w = '3456'
# print('Union:', s.union(l))   #{1,2,3,4,5,6}
# print('Intersection:', s.intersection(t))   #{3,4}
# print('Difference:', s.difference(s2)) #{1,2}
# print('Symmetric Difference:', s.symmetric_difference(d)) #{1,2,5,6}
# print('Union:', s.union(w))  #{1,2,3,4,'3','4','5','6'} 
# print('Union:', s.union(r))   #{1, 2, 3, 4, 5, 6}


# # Dict Methods 
d = {}
# d.update(5) #not iterable, so it will throw an error
# d.update(5.4) #not iterable, so it will throw an error
# d.update(4+5j) #not iterable, so it will throw an error
# d.update(True) #not iterable, so it will throw an error
# d.update(None)  #not iterable, so it will throw an error
# d.update([1,2,3]) #not iterable, so it will throw an error
# d.update((4,5,6)) #not iterable, so it will throw an error
# d.update({7,8,9}) #not iterable, so it will throw an error
# d.update('rak') #not iterable, so it will throw an error
# d.update(range(10, 14)) #not iterable, so it will throw an error
# d.update({10:'j', 11:'k', 12:'l'}) 
# print(d)
# d.update([ [1,'a'], (2,'b'), 'ab' ])
# print(d)
# d.update(( 'ra', 'ke', 'sh' ))
# print(d)
# d.update({ (3,'c'), (4,'d') })
# print(d)
# d.update({3:'f', 4:'g'})
# print(d)

# # #pop 
# d = {3:'c', 2:'b', 1:'a', 4:'d'}
# x = d.pop(2) 
# print(x) #output: b value of key 2 is removed from the dictionary
# # y = d.pop(100)
# # print(y) #output: KeyError: 100, since key 100 is not present in the dictionary
# z = d.pop(100, -1)
# print(z) #output: -1, since key 100 is not present in the dictionary

#popitem
# d = {3:'c', 2:'b', 1:'a', 4:'d'}
# x = d.popitem()
# print(x, d)  #  (4:'d'), {3:'c', 2:'b', 1:'a', 4:'d'} the last inserted key-value pair is removed from the dictionary and returned as a tuple
# y = d.popitem()
# print(y, d)

# #clear
# d = {3:'c', 2:'b', 1:'a', 4:'d'} 
# d.clear() 
# print(d) #clear all the elements from the dictionary, output: {}

# #get 
# d = {3:'c', 2:'b', 1:'a', 4:'d'}
# x = d.get(2)
# print(x, d) #b value of key 2 is returned from the dictionary b{3:'c', 2:'b', 1:'a', 4:'d'}
# y = d.get(100)
# print(y, d) #None {3: 'c', 2: 'b', 1: 'a', 4: 'd'}
# z = d.get(100, -1)
# print(z, d) #-1 {3: 'c', 2: 'b', 1: 'a', 4: 'd'}

# #setdefault
# d = {3:'c', 2:'b', 1:'a', 4:'d'}
# x = d.setdefault(2)
# print(x, d) #b{3:'c', 2:'b', 1:'a', 4:'d'}
# y = d.setdefault(100)
# print(y, d) #None {3: 'c', 2: 'b', 1: 'a', 4: 'd', 100: None}
# z = d.setdefault(90, -1)
# print(z, d) #-1 {3: 'c', 2: 'b', 1: 'a', 4: 'd', 100: None, 90: -1} 
# m = d.setdefault(90, -2)
# print(m, d) #-1 {3: 'c', 2: 'b', 1: 'a', 4: 'd', 100: None, 90: -1}