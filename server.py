from flask import Flask, request, jsonify
import math

app = Flask(__name__)
host = "localhost"
port = 8489
stack = list()
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
        return int(int(array_of_numbers[0]) / int(array_of_numbers[1]))
    elif operation == "pow":
        return pow(int(array_of_numbers[0]), int(array_of_numbers[1]))
    elif operation == "abs":
        return abs(int(array_of_numbers[0]))
    elif operation == "fact":
        return math.factorial(array_of_numbers[0])


@app.route('/stack/size', methods=['GET'])
def get_stack_size():
    return str(len(stack)), 200


@app.route('/stack/arguments', methods=['PUT'])
def add_arguments():
    content = request.json
    array_of_numbers = content['arguments']
    for number in array_of_numbers:
        stack.append(int(number))
    return str(len(stack)), 200


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
            return str(calc(array_of_numbers, operation))

    else:
        return "Error: unknown operation: " + operation


@app.route('/stack/operate', methods=['GET'])
def invoke_operation():
    operation = request.args.get('operation').lower()
    if operation in operations_with_two_numbers:
        if len(stack) < 2:
            return "Error: cannot implement operation" + operation + ". It requires 2 " \
                    "arguments and the stack has only " + str(len(stack)) + " arguments", 409
        array_of_numbers = [stack.pop(), stack.pop()]
        if array_of_numbers[1] == 0 and operation == "divide":
            return "Error while performing operation Divide: division by 0", 409
        else:
            return str(calc(array_of_numbers, operation))

    elif operation in operations_with_one_number:
        if len(stack) < 1:
            return "Error: cannot implement operation" + operation + ". It requires 1 " \
                    "arguments and the stack has only" + str(len(stack)) + "arguments", 409
        array_of_numbers = [stack.pop()]
        if array_of_numbers[0] < 0 and operation == "fact":
            return "Error while performing operation Factorial: not supported for the negative number", 409
        else:
            return str(calc(array_of_numbers, operation))
    else:
        return "Error: unknown operation: " + operation, 409


@app.route('/stack/arguments', methods=['DELETE'])
def delete_from_stack():
    count = int(request.args.get('count'))
    if len(stack) < count:
        return "Error: cannot remove " + str(count) + " from the stack. It has only " + str(len(stack)) + " arguments", 409
    for i in range(count):
        stack.pop()
    return str(len(stack)), 200


if __name__ == '__main__':
    app.run(host=host, port=port)
