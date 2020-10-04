#!/usr/bin/env python3
# [HARD]
# Good morning! Here's your coding interview problem for today.
# This problem was asked by Airbnb.
# Given a list of integers, write a function that returns the 
# largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6,
# and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# Follow-up: Can you do this in O(N) time and constant space?

def max_sum(array):
	incl = 0 # O(1) space
	excl = 0
	for i in array: # O(n) time
		new_excl = max(incl, excl)
		incl = i + excl
		excl = new_excl	
	return max(incl, excl)  

def main():
	array = [0, 12, 4, 18, 20, 56]
	print(array)
	print(max_sum(array))

if __name__ == '__main__':
	main()
