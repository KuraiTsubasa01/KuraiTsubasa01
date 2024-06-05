#'import module' vs. 'from module import names'.
#          Description                   Example import statement         Using imported names
#Import an entire module            |        import HTTPServer       | print(HTTPServer.address)
#Import specific name from a module | from HTTPServer import address | print(address)

#Using the from keyword to import specific names.
from hashlib import md5, sha1

text = input("Enter text to hash ('q' to quit): ")

while text != 'q':
    algorithm = input('Enter algorithm (md5/sha1): ')
    if algorithm == 'md5':
        output = md5(text.encode('utf-8'))
    elif algorithm == 'sha1':
        output = sha1(text.encode('utf-8'))
    else:
        output = 'Invalid algorithm selection'
    print('Hash value:', output.hexdigest())

    text = input("\nEnter text to hash ('q' to quit): ")


#Extending the hash example.
# FIXME: Import sha224 also
from hashlib import md5, sha1

text = input("Enter text to hash ('q' to quit): ")

# Add sha224 to prompt
algorithm = input('\nEnter algorithm (md5/sha1): ')
if algorithm == 'md5':
    output = md5(text.encode('utf-8'))
elif algorithm == 'sha1':
    output = sha1(text.encode('utf-8'))
    # FIXME: Add check for sha224
else:
    output = 'Invalid algorithm selection'

print('\nHash value:', output.hexdigest())



