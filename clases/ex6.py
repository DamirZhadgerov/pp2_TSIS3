def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Test the filter function with lambda
if __name__ == "__main__":
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    prime_numbers = list(filter(lambda x: is_prime(x), numbers))
    print("Prime numbers in the list:", prime_numbers)
