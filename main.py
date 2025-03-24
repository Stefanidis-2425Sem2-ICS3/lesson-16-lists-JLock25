# Name: J. Lockey
# Title: random number
# Date: March 24, 2025
# Description: This program takes 100 random numbers from 1-100 and finds the average between them all
import random
random_numbers = [random.randint(1, 100) for i in range(100)]
average = sum(random_numbers) / len(random_numbers)
print(f"Random numbers: {random_numbers}")
print(f"Average of the random numbers are: {average}")
