#Dictionaries

#Common dict operations.
#my_dict[key]
#Indexing operation – retrieves the value associated with key.
jose_grade = my_dict['Jose']

#my_dict[key] = value
#Adds an entry if the entry does not exist, else modifies the existing entry.
my_dict['Jose'] = 'B+'

#del my_dict[key]
#Deletes the key entry from a dict.
del my_dict['Jose']

#key in my_dict
#Tests for existence of key in my_dict.
if 'Jose' in my_dict: # ...

#Dictionary example: Gradebook.
student_grades = {}  # Create an empty dict
grade_prompt = "Enter name and grade (Ex. 'Bob A+'):"
menu_prompt = ("1. Add/modify student grade\n"
                "2. Delete student grade\n"
                "3. Print student grades\n"
                "4. Quit\n")

while True:  # Exit when user enters no input
    command = input(menu_prompt).lower().strip()
    if command == '1':
        name, grade = input(grade_prompt).split()
        # ...
    elif command == '2':
        # ...
    elif command == '3':
        # ...
    elif command == '4':
        break
    else:
        print('Unrecognized command.')

#Delete from dictionary.
user_input = input()
entries = user_input.split(',')
country_capital = {}

for pair in entries:
    split_pair = pair.split(':')
    country_capital[split_pair[0]] = split_pair[1]
    # country_capital is a dictionary, Ex. { 'Germany': 'Berlin', 'France': 'Paris'

del country_capital['Prussia']

print('Prussia deleted?', end=' ')
if 'Prussia' in country_capital:
    print('No.')
else:
    print('Yes.')

print ('Spain deleted?', end=' ')
if 'Spain' in country_capital:
    print('No.')
else:
    print('Yes.')

print ('Togo deleted?', end=' ')
if 'Togo' in country_capital:
    print('No.')
else:
    print('Yes.')