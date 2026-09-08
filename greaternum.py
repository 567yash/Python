
#Method 1
n1 = int(input())
n2 = int(input())
n3 = int(input())
# if n1>n2>n3:
#     print(n1, "is the greatest number")
# elif n2>n1>n3:
#     print(n2,"is the greatest number")
# else:
#     print(n3," is the greatest number")


#Method 2
if n1>n2 and n1>n3 :
    print(n1, "=n1 is greatest number" )
elif n2>n1 and n2>n3 :
    print (n2,"=n2 is greatest number")
else:
    print(n3,"=n3 is biggest number")