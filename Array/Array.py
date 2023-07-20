from array import *

array1 = array('i',[10,20,30,40,50])

print(array1)  # array('i',[10,20,30,40,50])

for i in array1:
    print(i,end=" ")   # 10 20 30 40 50

# Accessing Array Element

print(array1[0]) # 10
print(array1[2]) # 50

# to insert elemnet in array use insert built-in method 
# arrayName.insert(position , new element)

array1.insert(1,15) #insert 15 at position 1  "remember array is zero based index that means it starts with index 0"

for i in array1:
    print(i,end=" ")  # 10 15 20 30 40 50


print("\n") #add an empty line 

# Deletion Operation

array1.remove(40) # remove the element which is equal to 40

for x in array1:
   print(x, end=" ")  # 10 15 20 30 50

# Search Operation

# You can perform a search for an array element based on its value or its index.

print(array1.index(30)) # 3

# Update Operation

# Update operation refers to updating an existing element from the array at a given index.

array1[2] = 80

for x in array1:
   print(x, end=" ")  # 10 15 80 30 50

   
