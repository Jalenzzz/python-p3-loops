#!/usr/bin/env python3

# Function for counting down to "Happy New Year"
def happy_new_year():
    count = 10
    while count >= 1:
        print(count)
        count -= 1
    print("Happy New Year!")

# Function to square integers in a list
def square_integers(int_list):
    squared_list = []

    for num in int_list:
            squared_list.append(num ** 2)
    return squared_list

# Function for FizzBuzz
def fizzbuzz():
     for num in range(1, 101):
          if num % 3 == 0:
               print('Fizzbuzz')
          elif num % 3 == 0:
               print('Fizz')
          elif num % 5 == 0:
               print('Buzz')
          else:
               print(num)          

# Call the "Happy New Year" countdown function
happy_new_year()

# Calling the function with a list of integers
result = square_integers([1, 2, 3, 4, 5])
print(result)

# Call the FizzBuzz function
fizzbuzz()