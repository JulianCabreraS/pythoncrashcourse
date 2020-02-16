squares =[]

for value in range(1,11):
    square = value **2
    squares.append(square)

print(squares)

digits = [1,2,3,4,5,6,7,8,9]
print(min(digits))

print(max(digits))

#Using comprehension
squares= [value**2 for value in range(1,11)]
print(squares)

for value in range(1,1000000):
    print(value)

#To make list
numbers = list(range(1,1000000))
print(sum(numbers))