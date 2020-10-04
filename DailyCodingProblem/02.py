#!/usr/bin/env python3
# HARD
# Good morning! Here's your coding interview problem for today.
# This problem was asked by Uber.
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

import sys

def modify(array):
	length = len(array)
	modified = [1] * length # O(n) space
	temp = 1
	for i in range(length): # O(n) time
		modified[i] *= temp
		temp *= array[i]
	temp = 1
	for i in range(length-1, -1, -1): #O(n) time
		print(i)
		modified[i] *= temp
		temp *= array[i]
	return modified
	
def main():
	arguments = sys.argv[1:]
	array = []
	for arg in arguments:
		array.append(int(arg))
	print(array)

	print(modify(array))

if __name__ == '__main__':
	main()
