list1 = [2,4,5,2,1,4,6,7,1,2,5,3,2,1,6]
new_list = []

for element in list1:
    if element not in new_list:
        new_list.append(element)

    else:
        pass

print(new_list)
  