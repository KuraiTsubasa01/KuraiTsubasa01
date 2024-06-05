#List slicing

#List slice notation.
boston_bruins = ['Tyler', 'Zdeno', 'Patrice']
print('Elements 0 and 1:', boston_bruins[0:2])
print('Elements 1 and 2:', boston_bruins[1:3])
#Elements 0 and 1: ['Tyler', 'Zdeno']
#Elements 1 and 2: ['Zdeno', 'Patrice']

#List slicing: Using negative indices
election_years = [1992, 1996, 2000, 2004, 2008]
print(election_years[0:-1])  # Every year except the last
print(election_years[0:-3])  # Every year except the last three
print(election_years[-3:-1])  # The third and second to last years
#[1992, 1996, 2000, 2004]
#[1992, 1996]
#[2000, 2004]

#Some common list slicing operations
#my_list[start:end]
#Get a list from start to end (minus 1).
my_list = [5, 10, 20]
print(my_list[0:2])
#[5, 10]

#my_list[start:end:stride]
#Get a list of every stride element from start to end (minus 1).
my_list = [5, 10, 20, 40, 80]
print(my_list[0:5:3])
#[5, 40]

#my_list[start:]
#Get a list from start to end of the list.
my_list = [5, 10, 20, 40, 80]
print(my_list[2:])
#[20, 40, 80]

#my_list[:end]
#Get a list from beginning of list to end (minus 1).
my_list = [5, 10, 20, 40, 80]
print(my_list[:4])
#[5, 10, 20, 40]

#my_list[:]
#Get a copy of the list.
my_list = [5, 10, 20, 40, 80]
print(my_list[:])
#[5, 10, 20, 40, 80]