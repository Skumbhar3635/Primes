def is_prime(number):
    if number < 2:  # Numbers less than 2 are not prime
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:  # If the number is divisible by any i, it's not prime
            return False
    return True

# Example usage
number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is prime.")
else:
    print(f"{number} is not prime.")
