#Day 2
import math
# Variables in Python
first_name = 'Asabeneh' #type = str
last_name = 'Yetayeh'   #type = str
full_name = (first_name, last_name)
country = 'Finland' #type = str
city = 'Helsinki'   #type = str
age = 250  #type = int
year = 2024 #type = int
is_married = True #type = Bool
is_ligtht_on = False #type = Bool
skills = ['HTML', 'CSS', 'JS', 'React', 'Python'] #type = list
person_info = {
    'firstname':'Asabeneh', 
    'lastname':'Yetayeh', 
    'country':'Finland',
    'city':'Helsinki'
    } #type = dict

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True
#Quesion 4 
num_one = 5
num_two = 4

total = sum([num_one, num_two])
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = math.pow(num_one, num_two)
floor_division = num_one // num_two

#Question 5
radius = float(input("Enter radius: "))
area_of_circle = math.pi * math.pow(radius, 2 )
circum_of_circle = math.pi * (radius * 2)

print("Area of circle is: ", area_of_circle)
print("Circumference is: ", circum_of_circle)



