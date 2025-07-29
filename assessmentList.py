'''
# WAP to remove to find duplicates elements in list,
l1 = [1,2,2,3,4,5,5,5]
for i in l1:
    if l1.count(i)>=2:
        del[i]
    else:
        print([i],end="")
'''




'''
# WAP to sort the given list
l1 = [67,21,12,43,77,99,78]
l1.sort()
print(l1)
'''





 # WAP to create a list such that new list contains alternate even and odd from given list





'''
# Write a Python program to get the largest number from a list.
l1 = [21,67,45,18,71]
print(max(l1))
'''

        



'''
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']           Expected Output : ['Green', 'White', 'Black']


sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(sample_list[1:4])
'''






# Write a Python program to find the list of words that are longer than given words
colors =  ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
input_word = "Pink"

result = []

for color in colors:
    if len(color[:]) > len(input_word):
        result.append(color)

print("Word longer than input word:",result)
    










