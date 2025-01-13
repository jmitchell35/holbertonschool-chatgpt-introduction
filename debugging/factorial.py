#!/usr/bin/python3
import sys

def factorial(n):
	if not isinstance(n, int):
		raise TypeError("Factorial requires an integer input")
# raise is used to deliberately trigger an exception when something goes wrong
# it is hence a way to handle errors
	if n < 0:
	 	raise ValueError("Factorial cannot be calculated for negative numbers")
# TypeError and ValueError handle different types of errors.
# However, they both 

	result = 1
	while n > 1:
		result *= n
		n -= 1 # missing decrement
	return result
# similar behavior as C

def main():
# Good practice, prevents code from executing when the file is imported as a
# module
	try:
#Error handling : try / except allows trying code and gracefully handling errs
		if len(sys.argv) != 2:
			print("Usage: ./script.py <positive_integer>")
			sys.exit(1)
		n = int(sys.argv[1])
		f = factorial(n)
		print(f)

	except ValueError as e:
# e could be replaced with anything. It is meant to capture err message
		print(f"Error: please provide a valid integer: {e}")
		sys.exit(1)

if __name__ == "__main__":
	main()
# Entry point control : main is not called automatically when file is imported
# It is however when file is ran as executable
