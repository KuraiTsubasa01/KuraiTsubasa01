#my_list = [1, 2, 3]
#Creates a list.
my_list = [1, 2, 3]
print(my_list)

#list(iter)
#Creates a list.
my_list = [1, 2, 3]
print(my_list)

#my_list[index]
#Get an element from a list.
my_list = [1, 2, 3]
print(my_list[1])

#my_list[start:end]
#Get a new list containing some of another list's elements.
my_list = [1, 2, 3]
print(my_list[1:3])

#my_list1 + my_list2
#Get a new list with elements of my_list2 added to end of my_list1.
my_list = [1, 2] + [3] 
print(my_list)

#my_list[i] = x
#Change the value of the ith element in-place.
my_list = [1, 2, 3]
my_list[2] = 9 
print(my_list)

#my_list[len(my_list):] = [x]
#Add the elements in [x] to the end of my_list. 
#The append(x) method (explained in another section) may be preferred for clarity.
my_list = [1, 2, 3]
my_list[len(my_list):] = [9]
print(my_list)

#del my_list[i]
#Delete an element from a list.
my_list = [1, 2, 3]
del my_list[1]
print(my_list)