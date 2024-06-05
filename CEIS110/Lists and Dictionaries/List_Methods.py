#List Methods

#Adding elements

#list.append(x)
#Add an item to the end of list.
my_list = [5, 8]
my_list.append(16)

#list.extend([x])
#Add all items in [x] to list.
my_list = [5, 8]
my_list.extend([4, 12])

#list.insert(i, x)
#Insert x into list before position i.
my_list = [5, 8]
my_list.insert(1, 1.7)


#Removing elements

#list.remove(x)
#Remove first item from list with value x.
my_list = [5, 8, 14]
my_list.remove(8)

#list.pop()
#Remove and return last item in list.
my_list = [5, 8, 14]
val = my_list.pop()

#list.pop(i)
#Remove and return item at position i in list.
my_list = [5, 8, 14]
val = my_list.pop(0)


#Modifying elements

#list.sort()
#Sort the items of list in-place.
my_list = [14, 5, 8]
my_list.sort()

#list.reverse()
#Reverse the elements of list in-place.
my_list = [14, 5, 8]
my_list.reverse()


#Miscellaneous

#list.index(x)
#Return index of first item in list with value x.
my_list = [5, 8, 14]
print(my_list.index(14))

#list.count(x)
#Count the number of times value x is in list.
my_list = [5, 8, 5, 5, 14]
print(my_list.count(5))


#In-place modification using list methods.
vals = [1, 4, 16]

vals.append(9)
vals.insert(2, 18)
value = vals.pop()
vals.remove(4)
vals.remove(55)
#vals is a list containing elements 1, 4, and 16.
#The statement vals.append(9) appends element 9 to the end of the list.
#The statement vals.insert(2, 18) inserts element 18 into position 2 of the list.
#The statement vals.pop() removes the last element, 9, from the list.
#The statement vals.remove(4) removes the first instance of element 4 from the list.
#The statement vals.remove(55) removes the first instance of element 55 from the list. 
#The list does not contain the element 55 so vals is the same.