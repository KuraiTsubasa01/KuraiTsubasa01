triangle_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n'))
print('')

for row in range(1, triangle_height + 1):
    for col in range(row):
        print('{}'.format(triangle_char), end = ' ')
    print()
