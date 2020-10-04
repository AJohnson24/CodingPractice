#!/usr/bin/env python3
# EASY
# Good morning! Here's your coding interview problem for today.
# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

import sys

def find(numbers, target):
	table = {} # O(n) space
	for num in numbers: # O(n) time
		diff = target - num
		if diff in table:
			return True
		table[num] = diff
	return False

def main():
	arguments = sys.argv[1:]
	numbers = []
	length = len(arguments)

	for arg in range(length - 1):
		numbers.append(int(arguments[arg]))
	target = int(arguments[length - 1])

	print(find(numbers, target))

if __name__ == '__main__':
	main()
