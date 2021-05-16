a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = a[1:3]
print(b)

b = a[2:] 
print(b)

b = a[:3] 
print(b)

a[0:3] = [0] 
print(a)

b = a[::2]
print(b)

a = a[::-1] 
print(a)

b = a[:] 
print(b)