#Varied amount of input data

#input user values
user_input = input()

#split string
tokens = user_input.split()

#add tokens to a list
input_data = []
for token in tokens:
    input_data.append(int(token))
    
sum = 0
average = 0
max = 0
for i in input_data:
    sum = sum + i
    if i > max:
        max = i
average = sum/len(input_data)

print('{:.0f} {}'.format(average, max))