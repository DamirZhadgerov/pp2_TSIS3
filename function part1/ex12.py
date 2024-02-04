def histogram(numbers):
    for num in numbers:
        print('*' * num)

# Read the numbers from the user input
user_input = input("Enter a list of integers separated by spaces: ")
numbers = [int(num) for num in user_input.split()]

# Call the histogram function
histogram(numbers)

