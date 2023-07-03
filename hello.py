class Calculator:
    def __ini__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            print('cannot divide by zero')


calculator = Calculator()


result_add = calculator.add(5, 3)
result_subtract = calculator.subtract(8, 4)
result_multiply = calculator.multiply(2, 6)
result_divide = calculator.divide(10, 2)


print("Addition:", result_add)
print("Subtraction:", result_subtract)
print("Multiplication:", result_multiply)
print("Division:", result_divide)
