def solve(numheads, numlegs):
    # Initialize variables for chickens and rabbits
    num_chickens = 0
    num_rabbits = 0

    # Iterate through possible number of chickens
    for num_chickens in range(numheads + 1):
        # Calculate the number of rabbits
        num_rabbits = numheads - num_chickens

        # Calculate total legs based on current number of chickens and rabbits
        total_legs = 2 * num_chickens + 4 * num_rabbits

        # Check if the total legs match the given number of legs
        if total_legs == numlegs:
            # Return the number of chickens and rabbits
            return num_chickens, num_rabbits

    # If no solution found, return None
    return None, None

# Test the function
if __name__ == "__main__":
    numheads = 35
    numlegs = 94
    chickens, rabbits = solve(numheads, numlegs)
    if chickens is not None and rabbits is not None:
        print(f"Number of chickens: {chickens}")
        print(f"Number of rabbits: {rabbits}")
    else:
        print("No solution found.")
