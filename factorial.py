def factorial(n):
	total = 1
	if(n<0):
		print('Factorial of a negative number is not valid')
		return

	for i in range(2, n+1):
		total *= i
	return total

num = input("Enter a number to get it's factorial : ")
try:
    num = int(num)
except:
    print('Enter an integer')

if(isinstance(num, int) and num < 101):
	print(factorial(num))
else:
	print("We do up to 100")