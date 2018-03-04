# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


x = 1
total = 0

while x < 1000:
	xrem = x % 3
	xrem2 = x % 5
	if xrem == 0 or xrem2 == 0:
		total = total +x
	x = x + 1
	

print(total)