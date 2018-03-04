# Problem 6
# Find the difference between the sum of the squares of the first 100 natural 
# numbers and the square of sum.
# 
# sum of squares ex: (1)^2 + (2)^2 + (3)^2 .......(100)^2 = 338350
# square of sum ex: (1+2+3......100)^2 = 25502500
sumofSquare = 0
squareofSum = 0
temp = 0
temp2 = 0

for i in range(1,101): 							# for loop for i = 1,2,3.......,100.
	temp = i*i  								# 1^2, 2^2, 3^2
	sumofSquare = sumofSquare + temp2			# 1^2 + 2^2 + 3^2
	temp2 = temp2 + i 							# 1+2+3+4

squareofSum = temp2*temp2 
total = squareofSum - sumofSquare

print("Total of Square of Sum: " + str(squareofSum))
print("Total of Sum of Square: " + str(sumofSquare))
print(total)