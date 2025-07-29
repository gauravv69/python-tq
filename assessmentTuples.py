# Write a Python program to create a tuple.
a = (10, 20, 30, 40, 50)
print(a)


# Write a Python program to create a tuple with different data types
b = (10, "Gaurav", 1.15, True)
print(b)


# Write a Python program to unpack a tuple in several variables.
c = (10, 20, 30)
d, e, f = c
print("d:",d)
print("e:",e)
print("f:",f)


# Write a Python program to add an item in a tuple.
g = (1, 2, 3, 4, 5)
l1 = list(g)
l1.append(6)
g = tuple(l1)
print(g)


# Write a Python program to convert a tuple to a string.
t1 = (1, 2, 3, 4, 5)
s1 = list(t1)
print(s1)



# Write a Python program to reverse a tuple.
t2 = (2, 4, 6, 8, 10)
result = sorted(t2, reverse=True)
print(result)

t3 = (2, 4, 6, 8, 10)
result2 = t3[::-1]
print(result2)



# Write a Python program to convert a list to a tuple.
lst1 = [1, 2, 3, 4]
tup1 = tuple(lst1)
print(tup1)



# Write a Python program to remove an item from a tuple.
tup2 = (10, 20, 30, 40, 50)
lst = list(tup2)
lst.pop(2)
tup3 = tuple(lst)
print(tup3)



# Write a Python program to slice a tuple.
tupl = (1, 2, 3, 4, 5, 6)
slc = tupl[2:5]
print(slc)
slc2 = tupl[::2]
print(slc2)
















