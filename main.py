def collatz(x):
	print(x)
	if x <= 1:
		print ("Finished!")
		return 	
	elif x % 2 == 0:
		return collatz(x // 2)
	else:
		return collatz((3 * x) + 1)

print("Type an integer to see its Collatz conjecture series. Type 0 to quit.")

while 1: 
	userInput = int(input())
	if userInput <= 0:
		exit()
	print("Performing Collatz conjecture on", userInput)
	collatz(userInput)