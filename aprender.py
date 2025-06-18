# Variable string, interger, float, boolean

full_name = "Elias" # String
age = 25  # interger
gpa = 3.2 # float
is_student = True # True/Flase needs to be capital (Boolean)

print(f"Hello, {full_name}") # printing a variable 
print(f"You are {age} years old")
print(f"Your gpa is {gpa}")
print(f"Are you a student: {is_student}")
#if statement formating 
if is_student:
    print("You are a student")
else:
    print("You are not a student")

# arithmatic
# + addition
# - subtraction
# * multiplication
# / division (returns a float)
# // interger division (always returns a interger) 
# % remainder 

friends = 5 

friends= friends + 1 # also can do += 1

fiends = friends - 1 # also can use -= 1

friends =  friends * 2 # also can use *= 1 

firends = friends / 2 # also can do /= 2

firends = friends // 2 # also can do //=

remaining_friends = friends % 3 

print(remaining_friends)

print(friends)

# typecasting = converting a variable into a different data type

name = "Bro code"
edad = 25
gpaa = 3.2
si_estudiente = False

print(type(gpaa)) # prints the type 

gpa = int(gpa)

print(gpa)

edad = float(edad)

print(edad)

edad = str(edad)

print(edad)

name = bool(name)

print(name)

#input 

name = input("Enter your name: ")
age = int(input("Enter your age: ")) # would still be a stirng although it is a number so nos cambiamos
age += 1

print(f" Hello, {name}!")
print(f"You are {age} years old")

# if statements if, elief, else

age = int(input("Enter your age: "))
has_ticket = False
if age >= 18:
    print("You are an adult")
elif age < 0:
    print("How tf are you even doing this ho")
elif age == 0: # to see if a value is exactly equal
    print("You were  just born")

else:
    print("You are a child..")

if has_ticket:
    print("You may enter")
else:
    print("You need a ticket")