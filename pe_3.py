# Problem:
# the prime factors of 13195 are 5, 7, 13, 29
# What is the largest prime factor of the number 600851475143?

num = 600851475143
b = 2
c = 0
while num != 1: 
	rem = num % b
	if rem == 0:
		num = num / b
		c = b
		b = 2
	b = b + 1		

print(c)

