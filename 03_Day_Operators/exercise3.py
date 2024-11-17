import math
age = 20
height = 5.4
complex_number = 3 + 2j

def area_of_triangle(base,height):
    area = 0.5 * base * height
    return area

def euclidean_distance(x,y):
    return math.dist(x,y)

def slope(x1,y1,x2,y2):
    return ((y2-y1)/(x2-x1))

def slope_and_y_intercept(equationOfLine):
    equationOfLine = equationOfLine.replace(" ", "")
    
    # Check if the equation starts with 'y='
    if not equationOfLine.startswith("y="):
        print("Invalid equation format. Please use the format y=mx+c.")
        return None, None
    
    # Remove 'y=' from the equation
    equationOfLine = equationOfLine[2:]
    
    
    if 'x' not in equationOfLine:
        print("Invalid equation format. Missing 'x'.")
        return None, None
    
    parts = equationOfLine.split('x')
    
    # Extract gradient (m)
    m_part = parts[0]
    if m_part == "":
        m = 1.0  # Default to 1 if it's just 'x'
    elif m_part == "-":
        m = -1.0  # Default to -1 if it's '-x'
    else:
        m = float(m_part)  # Convert to float
    
    # Extract y-intercept (c)
    c_part = parts[1] if len(parts) > 1 else "0"
    c = float(c_part) if c_part else 0.0  # Default to 0 if no intercept
    
    return m, c

def value_of_y(x):
    return (x ** 2) + (6 * x) + 9

#Question 12
print(len("python") > len("dragon") )

#Question 14
print("jargon" in "I hope this course is not full of jargon")

#Question 15
print("on" not in "python", "on" not in "dragon")

def is_even(number):
    if (number % 2) == 0:
        print(f"{number} is even")

    else:
        print(f"{number} is not even")     


def main():
    try:
        print("Choose an operation")
        print("1. Area of triangle")
        print("2. Euclidean distance")
        print("3. Gradient of a line given two points on the line")
        print("4. Slope and y-intercept")
        print("5. Value of y")
        print("6. Is even: ")

        selection = input("Please enter operation number: ")
        if selection == "1":
            base = float(input("Enter the base: "))
            height = float(input("Enter the height: "))
            area = area_of_triangle(base=base, height=height)
            print("The area of the triangle is: ", area)

        if selection == "2":
            x = list(map(float, input("Enter x cordinates:").split(",")))
            y = list(map(float, input("Enter y cordinate: ").split(","))) 
            euclidean = euclidean_distance(x=x, y=y)
            print("The euclidean distance is: ", euclidean)  

        if selection == "3":
            x1 = float(input("Please enter x1: "))  
            y1 = float(input("Please enter y1: ")) 
            x2 = float(input("Please enter x2: ")) 
            y2 = float(input("Please enter y2: "))
            gradient = slope(x1=x1,x2=x2,y1=y1,y2=y2)
            print("The gradient is: ", gradient) 

        if selection == "4":
            equation = input("Please enter the equation of line in the form y=mx+c: ")
            m, c = slope_and_y_intercept(equation)
            print(f"the gradient is {m} and y-intercept is {c}")  

        if selection == "5":
            x = float(input("Enter the value of x: ")) 
            value = value_of_y(x=x)
            print(f"The value of y is {value}") 

        if selection == "6":
            number = int(input("Enter number: "))
            even = is_even(number=number) 
            print(even)         

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()             