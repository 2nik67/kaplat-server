from flask import Flask, request, jsonify


app = Flask(__name__)
host = "localhost"
port = 8489
stack = []
operations = ["Plus", "Minus", "Times", "Divide", "Pow", "Abs", "Fact"]


# Plus ; binary operator ; x + y
# Minus: binary operator ; x - y
# Times: binary operator ; x * y
# Divide: binary operator; x / y
# Pow: binary operator ; x ^ y
# Abs: unary operator ; |x|
# Fact: unary operator ; x!

def calc(array_of_numbers):
    x = float(array_of_numbers[0]) + float(array_of_numbers[1])
    return x


@app.route('/independent/calculate', methods=['POST'])
def independent_calculation():
    content = request.json
    array_of_numbers = content['arguments']
    operation = content['operation']
    for operation_in_list in operations:
        if operation.casefold() == operation_in_list.casefold():
            return str(calc(array_of_numbers)), 200
            

@app.route('/independent/calculate', methods=['GET'])
def independent_calc2ulation():
    return "Hey"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host=host, port=port)
