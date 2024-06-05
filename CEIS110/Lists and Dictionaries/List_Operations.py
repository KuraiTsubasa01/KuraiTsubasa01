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

#In-place modification of a list.
my_teams = ['Raptors', 'Heat', 'Nets']
your_teams = my_teams  # Create a shared reference to same list

my_teams[1] = 'Lakers'  # Modify list element

print('My teams are:', my_teams)  # Both variables have changed
print('Your teams are:', your_teams)  # Both variables have changed


#In-place modification of a copy of a list.
my_teams = ['Raptors', 'Heat', 'Nets']
your_teams = my_teams[:]  # Assign your_teams with a COPY of my_teams
	
my_teams[1] = 'Lakers'  # Modify list element

print('My teams are:', my_teams)  # List element has changed
print('Your teams are:', your_teams)  # List element has not changed

#List indexing.
colors = ['red', 'green', 'blue']

colors[1] = 'yellow'  # Change list element
# print colors...

fav_color = colors[2]  # Bind to 'blue'
fav_color = 'turquoise'  # List not altered
# print colors...

#Modify short_names by deleting the first element and changing the last element to Joe.
#Sample output with input: 'Gertrude Sam Ann Joseph'
#['Sam', 'Ann', 'Joe']
user_input = input()
short_names = user_input.split()

del short_names[0]
short_names[2] = 'Joe'

print(short_names)