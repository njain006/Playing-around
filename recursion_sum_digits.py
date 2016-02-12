def sum_digits(num):
	
	if num == 0 : return 0

	print ("value",num/10)
	print ("modl",num%10)

	return sum_digits( num / 10) + num % 10

print (sum_digits(1111))