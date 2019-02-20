#!/usr/bin/python
input = 123

def addDigits(digits):
	x = 99
	sum = 0
	#no reversing needed
	while digits != 0:
		#get remainder to extract last number
		sum  += digits % 10
		#truncate
		digits = digits // 10
	return sum

print(addDigits(input))
