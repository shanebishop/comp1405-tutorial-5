#
# Shane Bishop
# 101030053
#
# Reference List:
# Gaddis, T. (2015). "Starting Out With Python"
#

# Test loop counter
loop_counter = 0

# Postconditional while loop for input
while True:
	# Loop counter testing
	loop_counter = loop_counter + 1
	
	# Retrive initial input
	user_input = input("Please enter a number between 1 and 10: ")
	
	# If the input is not a digit, try again
	if not (user_input.isdigit()):
		print("Sorry,", user_input, "is not a number. Please try again.")
		continue
	
	# Since the input is a digit, it can be converted from a string to an int
	num_rows = int(user_input)
	
	# Check to see if the initial input is incorrect
	if num_rows <= 0 and num_rows >= 10:
		print("Sorry,", num_rows, "is an invalid entry. Please try again.")
		continue
	# If the initial input is incorrect, draw the pyramid
	else:
		print()
		
		# Draw pyramid
		for i in range(1, num_rows + 1):
			for j in range(num_rows - i):
				print(" ", end="")
			for k in range(i):
				print(i, end="")
				print(" ", end="")
			for l in range(i):
				print(" ", end="")
			print()
		
		print()
		
		# Check to see if the user wants to draw another triangle
		print("Would you like to draw another triangle? ('Y' for yes and 'N' for no) ")
		keep_going = input().upper()
		
		# Test to see if the user wants to keep going
		if keep_going == "N":
			break
