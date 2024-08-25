# # This is a Python script demonstrating basic if-else statements and Python indentation.

# # First if-else statement
# if 2 > 2:
#     print("Five is greater than two!")  # This message should print if the condition is True
# else:
#     print("u are Free")  # This message should print if the condition is False

# # This line will always print regardless of the condition above
# print("Hi")

# # Second if-else statement
# if 4 != 4:
#     print("fdr")  # This message should print if the condition is True
# else:
#     print("hahah")  # This message should print if the condition is False




# This is a Python script demonstrating more complex control flow structures and indentation.

# Define a function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    
    # Check for divisibility by numbers from 2 to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # If the number is divisible by any other number, it's not prime
    
    return True  # If no divisors are found, the number is prime

# Function to print prime numbers up to a given limit
def print_primes(limit):
    print("Prime numbers up to", limit, ":")
    
    for num in range(2, limit + 1):
        if is_prime(num):  # Check if the number is prime using the is_prime function
            print(num)  # Print the prime number

# Main program
if __name__ == "__main__":
    # Get the limit from user input
    limit = int(input("Enter the limit to find prime numbers: "))
    
    # Call the print_primes function to print prime numbers up to the limit
    print_primes(limit)
