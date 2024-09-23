def lab1Question1(input_gb):
    # Convert the input of a number of gigabytes to the number of bytes
    num_bytes = input_gb*1024*1024*1024
    # Do the work here
    # The solution to this goes here (and in all of them below...)
    # Set the variable num_bytes to the answer and return it
    return num_bytes

def lab1Question2(name):
    # Take an input of a name, return True if there is an odd number of characters in the name, False otherwise
    # Return None if the input is not a string
    if not isinstance(name, str):
        return None
    is_odd = len(name) % 2 != 0
    return is_odd

def lab1Question3(input_string, input_number):
    # Take in two inputs - a string and a number
    # Return the character of the string in the index given by number.  If this index does not exist, then return -1.

    if 0 <= input_number < len(input_string):
        character_at = input_string[input_number]
    else:
        character_at = -1

    return character_at

def lab1Question4(file_name):
    # Take an input of a file name. 
    # Read that file and return a list of all numbers in that file
    list_of_nums = []
    with open(file_name, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word.isdigit():
                    list_of_nums.append(int(word))

    return list_of_nums

def lab1Question5(list_numbers):
    # Take an input of a list of numbers
    # Return the mode from that list. 
    from statistics import mode
    mode_of_list = mode(list_numbers)
    return mode_of_list

def lab1Question6(quarters, dimes, nickels, pennies):
    # Take in 4 inputs - the number of quarters, dimes, nickels, and pennies in a handful
    # Return the total amount in dollars
    # For example, if the handful contains 4 quarters, 3 dimes, 2 nickels, and 1 penny, the function should return 1.41.
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return total

## Example of calling a function to test these... 
# Question 1 Check:
in_gb = 10
expected_bytes = 10*1024*1024*1024
calculated_bytes = lab1Question1(in_gb)

print("Input gigabytes: ", in_gb)
print("Expected bytes: ", expected_bytes)
print("Calculated bytes: ", calculated_bytes)
if expected_bytes == calculated_bytes:
    print("Test passed")
else:
    print("Test failed")

# You can make similar tests to check if things work for you. 
# This is kind of annoying, I am aware, but it is a really important skill in programming. 
# Determining how to check if your code works, and define specific tests for what "working" means is 
# something that allows you to tackele any larger problem - you can break it into smaller bits, attack one bit at a time,
# check to ensure you've done it correctly, and then move on to the next bit.

# question2
name = "Alice"
expected_result = True  # "Alice" has 5 characters, so it is odd
calculated_result = lab1Question2(name)

print("Input name: ", name)
print("Expected result: ", expected_result)
print("Calculated result: ", calculated_result)
if expected_result == calculated_result:
        print("Test passed")
else:
        print("Test failed")

#question3
input_string = "hello"
input_number = 1
expected_character = "e"
calculated_character = lab1Question3(input_string, input_number)

print("Input string: ", input_string)
print("Input number: ", input_number)
print("Expected character: ", expected_character)
print("Calculated character: ", calculated_character)
if expected_character == calculated_character:
        print("Test passed")
else:
        print("Test failed")

# question4
file_name = "testfile.txt"
# Create a test file with some numbers
with open(file_name, "w") as file:
    file.write("42 apples, 17 bananas, and 3 oranges.")

    expected_result = [42, 17, 3]
    calculated_result = lab1Question4(file_name)

    print("Expected numbers: ", expected_result)
    print("Calculated numbers: ", calculated_result)
    if expected_result == calculated_result:
        print("Test passed")
    else:
        print("Test failed")

# question5
list_numbers = [1, 2, 2, 3, 3, 3]
expected_mode = 3
calculated_mode = lab1Question5(list_numbers)

print("Input list: ", list_numbers)
print("Expected mode: ", expected_mode)
print("Calculated mode: ", calculated_mode)
if expected_mode == calculated_mode:
        print("Test passed")
else:
        print("Test failed")

# question6
quarters, dimes, nickels, pennies = 4, 3, 2, 1
expected_total = 1.41
calculated_total = lab1Question6(quarters, dimes, nickels, pennies)

print("Input coins: ", (quarters, dimes, nickels, pennies))
print("Expected total dollars: ", expected_total)
print("Calculated total dollars: ", calculated_total)
if expected_total == calculated_total:
        print("Test passed")
else:
        print("Test failed")

