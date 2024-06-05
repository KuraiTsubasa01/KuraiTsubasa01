#List Iteration

#Iterating through a list.
for my_var in my_list:
    # Loop body statements go here

#Iterating through a list example: Finding the maximum even number.
# User inputs string w/ numbers: '203 12 5 800 -10'
user_input = input('Enter numbers:')

tokens = user_input.split()  # Split into separate strings

# Convert strings to integers
nums = []
for token in tokens:
    nums.append(int(token))

# Print each position and number
print()  # Print a single newline
for index in range(len(nums)):
    value = nums[index]
    print('{}: {}'.format(index, value))

# Determine maximum even number
max_num = None
for num in nums:
    if (max_num == None) and (num % 2 == 0):
        # First even number found
        max_num = num
    elif (max_num != None) and (num > max_num ) and (num % 2 == 0):
        # Larger even number found
        max_num = num

print('Max even #:', max_num)

#Using a variable to keep track of a value while iterating over a list.
nums = [1, 4, 15, 456]

max_even = None
for num in nums:
    if num % 2 == 0: # The number is even?        
        if max_even == None or num > max_even:  # Greatest even number seen?
            max_even = num

#Built-in functions supporting list objects.
#all(list)
#True if every element in list is True (!= 0), or if the list is empty.
print(all([1, 2, 3])) #True
print(all([0, 1, 2])) #False

#any(list)
#True if any element in the list is True.
print(any([0, 2])) #True
print(any([0, 0])) #False

#max(list)
#Get the maximum element in the list.
print(max([-3, 5, 25])) #25

#min(list)
#Get the minimum element in the list.
print(min([-3, 5, 25])) #-3

#sum(list)
#Get the sum of all elements in the list.
print(sum([-3, 5, 25])) #27

#Using built-in functions with lists
#Lebron James: Statistics for 2003/2004 - 2012/2013
games_played = [79, 80, 79, 78, 75, 81, 76, 79, 62, 76]
points = [1654, 2175, 2478, 2132, 2250, 2304, 2258, 2111, 1683, 2036]
assists = [460, 636, 814, 701, 771, 762, 773, 663, 502, 535]
rebounds = [432, 588, 556, 526, 592, 613, 554, 590, 492, 610]

# Print total points

# Print Average PPG

# Print best scoring years (Ex: 2004/2005)

# Print worst scoring years (Ex: 2004/2005)


#Get user guesses.
num_guesses = int(input())
user_guesses = []

for i in range(num_guesses):
    guess = int(input())
    user_guesses.append(guess)

print('user_guesses:', user_guesses)


#Sum extra credit
user_input = input()
test_grades = list(map(int, user_input.split())) # test_grades is an integer list of test scores


sum_extra = -999 # Initialize 0 before your loop

sum_extra = 0
for grade in test_grades:
    if grade > 100:
        sum_extra = sum_extra + (grade - 100)

print('Sum extra:', sum_extra)

#Hourly temperature reporting.
user_input = input()
hourly_temperature = user_input.split()

for index in range(len(hourly_temperature)):
    print(hourly_temperature[index], end=' ')
    if index!= (len(hourly_temperature)-1):
        print('->', end=' ')
print('')

