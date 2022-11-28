from flask import Flask, request, jsonify
import math

app = Flask(__name__)
host = "localhost"
port = 8489
stack = []
operations_with_two_numbers = ["plus", "minus", "times", "divide", "pow"]
operations_with_one_number = ["abs", "fact"]


# Plus ; binary operator ; x + y
# Minus: binary operator ; x - y
# Times: binary operator ; x * y
# Divide: binary operator; x / y
# Pow: binary operator ; x ^ y
# Abs: unary operator ; |x|
# Fact: unary operator ; x!

def calc(array_of_numbers, operation):
    if operation == "plus":
        return int(array_of_numbers[0]) + int(array_of_numbers[1])
    elif operation == "minus":
        return int(array_of_numbers[0]) - int(array_of_numbers[1])
    elif operation == "times":
        return int(array_of_numbers[0]) * int(array_of_numbers[1])
    elif operation == "divide":
        return int(array_of_numbers[0]) / int(array_of_numbers[1])
    elif operation == "pow":
        return pow(int(array_of_numbers[0]), int(array_of_numbers[1]))
    elif operation == "abs":
        return abs(int(array_of_numbers[0]))
    elif operation == "fact":
        return math.factorial(array_of_numbers[0])


@app.route('/independent/calculate', methods=['POST'])
def independent_calculation():
    content = request.json
    array_of_numbers = content['arguments']
    operation = content['operation'].lower()

    if operation in operations_with_two_numbers:
        if len(array_of_numbers) < 2:
            return "Error: Not enough arguments to perform the operation" + operation, 409
        elif len(array_of_numbers) > 2:
            return "Error: Too many arguments to perform the operation " + operation, 409
        elif operation == 'divide' and int(array_of_numbers[1]) == 0:
            return "Error while performing operation Divide: division by 0", 409
        else:
            return str(calc(array_of_numbers, operation))

    elif operation in operations_with_one_number:
        if len(array_of_numbers) < 1:
            return "Error: Not enough arguments to perform the operation" + operation, 409
        elif len(array_of_numbers) > 1:
            return "Error: Too many arguments to perform the operation " + operation, 409
        elif operation == "factorial" and int(array_of_numbers[0]) < 0:
            return "Error while performing operation Factorial: not supported for the negative number", 409

    else:
        return "Error: unknown operation: " + operation


@app.route('/independent/calculate', methods=['GET'])
def independent_calc2ulation():
    return "Hey"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host=host, port=port)
