def spy_game(nums):
    # Initialize variables to keep track of 0s encountered
    zero_count = 0
    # Iterate through the list
    for num in nums:
        # If the current number is 0, increment zero_count
        if num == 0:
            zero_count += 1
        # If we have seen two 0s and the current number is 7, return True
        elif num == 7 and zero_count >= 2:
            return True
    # If we reach here, we haven't found 007 sequence
    return False

# Test cases
print(spy_game([1,2,4,0,0,7,5]))  # True
print(spy_game([1,0,2,4,0,5,7]))   # True
print(spy_game([1,7,2,0,4,5,0]))    # False
