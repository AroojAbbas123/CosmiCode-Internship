# In this task we are going to fibd the prime factors of a user provided number

# Prime factors of a number are the prime numbers that multiply together to give the original number. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.



def prime_factor(n):
    factors = []
    small_prime= 2  # Start with the smallest prime
    
    while n > 1:
        while n % small_prime == 0:
            factors.append(small_prime)
            n = n // small_prime
        small_prime += 1  # Move to the next number
    
    return factors

# Example Usage
number =int(input("Enter a number: "))
print(f"Prime factors of {number}: {prime_factor(number)}")

    

    