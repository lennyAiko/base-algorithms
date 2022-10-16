### CONVERTING BASE 2 TO BASE 10

# collect user input

value = input("Enter the binary value: ")

# function to carry out operation

def converter(value, pow_value = 0, eval=[]):
    # returns a list 

    for i in value:
        num = 2**pow_value
        num = int(i) * num
        eval.append(num)
        pow_value += 1
    return eval

# show result

result = 0
eval = converter(value=value)

for x in eval:
    result += x

print(f"The result for converting {value} is: {result}")