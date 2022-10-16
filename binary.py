# Collect user input

value = int(input("Enter value you want to convert to binary: "))

# set up variables and list to store binary

binary_values = []
reminder = 0
divided_value = 0
count = 0

# perform modulos operation

for i in range(value-1):
    if count < 1:
        divided_value = value // 2
        reminder = value % 2
        count += 1
        binary_values.append(reminder)
    reminder = divided_value % 2
    divided_value = divided_value // 2
    binary_values.append(reminder)

print(f"The binary conversion of {value} is: ", end="")

binary = binary_values[::-1]

start = binary.index(1)

for i in binary[start:]:
    print(i, end="")




