for value in range(1, 5):
	print(value)
	
numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
	squares.append(value ** 2)
	
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**2 for value in range(1,11)]
print(squares)

for value in range(1, 21):
	print(value)

numbers = list(range(1,100))
for value in numbers:
	print(value)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_number = list(range(1,20,2))
print(odd_number)

three_numbers = []
for value in range(1,10):
	three_numbers.append(value *3)
print(three_numbers)

three_numbers = [value*3 for value in range(1,10)]
print(three_numbers)

cube_number = []
for value in range(1,10):
	print(value **3)
cube_number = [value ** 3 for value in range(1,10)]
print(cube_number)
