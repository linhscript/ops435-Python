#!/usr/bin/env python3

import sys

letter = str(sys.argv[1])

if len(letter) != 9:
	if len(letter) == 1:
		print("Sorry, " + letter + ' has only 1 letter.')
	else:
		print("Sorry, " + letter + ' has only ' + str(len(letter)) + ' letters.')
	print("Please give me a nine-letter word")
else:
	print ("Thank your for your cooperation.")
	odd_list = []
	even_list = []
	for i in range(len(str(letter))):
		if i % 2 == 0:
			odd_list.append(str(letter)[i])
	out_put = str(''.join(odd_list))
	reverse = out_put[::-1]

	print("Here is the enter code: " + out_put)
	print("And the exit code is: " + reverse)
	