list1 = [1, 2, 3, 4, 5, 6]

# accessing elements

print(list1[2])  # 3

del list1[0]  # element at index 0 will be deleted

print(list1)  # [2, 3, 4, 5, 6]

# add element at the end of the list

list1.append(7)
print(list1)  # [2, 3, 4, 5, 6,7]


# add element at specific  index

list1.insert(0, 1)
print(list1)  # [1,2, 3, 4, 5, 6,7]

# Concatenation

list2 = [8, 9, 10]

list3 = list1+list2
print(list3)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Repetition

list5 = ["Hi"] * 4
print(list5)  # ['Hi', 'Hi', 'Hi', 'Hi']

# Membership => check if the element exists in the array or not

print(3 in list1)  # True
