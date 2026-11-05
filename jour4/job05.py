def any_computation(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "%":
        return num1 % num2


print(any_computation(10, "+", 3))
print(any_computation(10, "-", 3))
print(any_computation(10, "*", 3))
print(any_computation(10, "/", 2))
print(any_computation(10, "%", 3))
