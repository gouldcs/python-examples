# Example 2.2
name = "Chris Evans"
age = 39
hotness_scale = (2 * 4) + 1.9

print(name, "is", age, "years old, but he is still a", hotness_scale, "out of 10 on the hotness scale.")

#Example 2.3
print('{0} is {1} years old, but he is still a {2} out of 10 on the hotness scale.'.format(name, age, hotness_scale))

# Example 2.6
name = "Chris Evans"
new_name = "Steve Rogers"
name = new_name


# Further Explorations
name = "Cameron"
age = 21
chocolate_lover = True
favorite_number = 2 * 11

# Problem 1
print("Welcome to the Avengers,", name)

# Problem 2
print('{0}, you are only {1}. To be an Avenger, you have to pass a test'.format(name, age))

# Problem 3
print('{0}, at {1} you have passed the test because your favorite number is {2}, and because \
       you have a {3} love for chocolate.'.format(name, age, favorite_number, chocolate_lover))

# Problem 4
rubiks_side_length = 6
cube_side_length = 6
side_length = 6

# Problem 5
"""
Python does not allow for variable declarations because the language does type
inference. In order to allow for variable declaration in Python, the language
would need to add a way to specify the type of a variable upon creation, or have
a command to declare a variable.
"""
