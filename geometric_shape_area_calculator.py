#geometric_shape_area_calculator

import math # DO NOT MODIFY

def main():
    circle_pi = math.pi # DO NOT MODIFY, this line of code is assigning the variable 'circle_pi' equal to Pi ~3.14
    user_Welcome = input('Welcome to the geometric shape area calculator!')
    choice = input('Select a shape by entering 1, 2, or 3')
    choice_value = int(choice)
    print(type(choice_value == int)
    #print(choice_value == 1 or choice_value == 2 or choice_value == 3) ## this line would also c
    # TODO: In terminal, print Welcome to the geometric shape area calculator!
    
    # User Options
    # Circle = 1
    # Rectangle = 2
    # Triangle = 3
    
    # TODO: Using one print statement, use string concatenation to print the options only 
    # as a single string (make sure to add a space between each option)
    print('Circle = 1' + 'Rectangle = 2' + 'Triangle = 3')
    # TODO: In terminal, ask the user "Select a shape by entering 1, 2, or 3' and assign the input to a new variable named 'choice'.

    # TODO: Convert the variable 'choice' to an integer data type.
    # TODO: With one line of code, verify the variable 'choice' is indeed the data type integer, use conditional logic and print the output.  If converted correctly, the output in Terminal should read 'True'.
  
    if choice == 1:  #DO NOT REMOVE THE 'IF'
        # Calculate the area of a circle
        radius = input('Please indicate the desired circle radius')
        radius_type = float(radius)
        area = circle_pi * radius_type ** 2 
        # TODO: Assign a new variable named 'radius' and ask for the user's input for the radius of the circle.
        # TODO: Convert 'radius' to float.
        # TODO: Assign a new variable named 'area' and implement the logic to calculate the area of a circle.
        # HINT 1 : The formula to find area of a circle: 'circle_pi' times radius squared.  
        # Hint 2 : circle_pi is a variable that has been assigned on Line 9 and equals Pi in math.  

    elif choice == 2: # DO NOT REMOVE THE 'ELIF'
        # Calculate the area of a rectangle
        length = input('Please indicate the desired length of the rectangle')
        width = input('Please indicate the desired width of the rectangl')
        dsr_length = float(length)
        dsr_width = float(width)
        area = dsr_length * dsr_width
        # TODO: Assign new variables 'length' and 'width' and ask for the user's input for the length and width of the rectangle.
        # TODO: Convert both 'length' and 'width' to float.
        # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a rectangle.
        # HINT: The formula to find the area of a rectangle: length times width

    elif choice == 3: #DO NOT REMOVE THE 'ELIF'
        # Calculate the area of a triangle
        base = input('Please indicate the desired base length of the triangle')
        height = input('Please indicate the desired height of the triangle')
        dsr_base = float(base)
        dsr_height = float(height)
        area = 1/2 * dsr_base * dsr_base
        # TODO: Assign new variables 'base' and 'height' and ask for the user's input for the base length and height of the triangle.
        # TODO: Convert both 'base' and 'height' to float.
        # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a triangle.
        # HINT: The formula to find the area of a Triangle: half times base times height

    else:
        # TODO: If the user enters anything other than 1, 2 or 3, print statement "Invalid choice ."
        print ('Invalid choice.')
    if choice in [1, 2, 3]: # DO NOT MODIFY
        print(f"The area is: {area:.2f} square units.") # DO NOT MODIFY

    # TODO: Print a statement explaining each step required to find and complete your technical assignments.  Be specific. 
print("1st: I used the input() function several times to greet and obtain information form the user directly in/from the terminal, see lns 7, 8, 29, 40, 41, 52, 53. submittions from users. 2nd: I assigned several variables to hold the numerical values entered enterd by users. These values were converted to floats and integers via pyton functions used for datatype conversion, int() and float(), see lns 9, 10, 29, 30, 40-43, 52-55 . 3rd: to perform the actual calculations of area that this program is designed to generate, I devised equations to compute the areas of circle, rectangle and triangle (see ln 31, 44, 56). 4th: in order to to control and assure that this progrma only processed the relevant information and provided the correct outputs, various conditional statements were used. see, lns 11 (an internal proof not conneccted to the programs function), 27, 38, 50. 5th: print() statements wer used to display several important outputs genertaed by this code principle among them is the provision of answers (i.e, areas)  of the three shapes, dependent upon the user's desired preferences")

if __name__ == "__main__": # DO NOT MODIFY
    main() # DO NOT MODIFY
