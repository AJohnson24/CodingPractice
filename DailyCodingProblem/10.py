#!/usr/bin/env python3
# Good morning! Here's your coding interview problem for today.
# This problem was asked by Apple.
# Implement a job scheduler which takes in a function f and an 
# integer n, and calls f after n milliseconds.
import time
import sys

def scheduler(f, n):
	print(f"waiting {n} milliseconds")
	time.sleep(n/1000)
	f()

def sequence():
	for i in range(0,10):
		print(i)


def main():
	arg = sys.argv[1]
	try:
		delay = int(arg)
	except ValueError:
		print("error: please enter an integer")
		exit(1)
	scheduler(sequence, delay)

if __name__ == '__main__':
	main()

