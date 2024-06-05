#A pedometer treats walking 1 step as walking 2.5 feet. Define a function named feet_to_steps that takes a float as a parameter, 
#representing the number of feet walked, and returns an integer that represents the number of steps walked. Then, write a main 
#program that reads the number of feet walked as an input, calls function feet_to_steps() with the input as an argument, and 
#outputs the number of steps.

#Use floating-point arithmetic to perform the conversion.

def feet_to_steps(user_feet) :
    return (int)(user_feet/2.5)

if __name__ == '__main__':
    input_feet = float(input())
    steps_walked = feet_to_steps(input_feet)
    print(steps_walked)