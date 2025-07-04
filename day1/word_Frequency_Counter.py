string = "Apple Mango Orange Mango Guava Guava Mango"

list1 = string.split()

print(list1)
count = dict()

for word in list1:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)
 


