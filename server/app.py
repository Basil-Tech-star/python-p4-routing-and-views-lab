#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>', methods=['GET'])
def print_string(text):
    print(text)
    #Display in the web browser
    return text

@app.route('/count/<int:num>', methods= ['GET'])
def count(num):
    #generating list of numbers from 1 to num
    numbers = '\n' .join(str(i) for i in range(num)) + '\n'
    #diplaying numbers on seperate lines
    return numbers

@app.route('/math/<int:num1>/<operation>/<int:num2>', methods=['GET'])
def math(num1,operation,num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div' and num2 != 0:
        result = num1 / num2
    elif operation == '%' and num2 != 0:
        result = num1 % num2
    else:
        return "Invalid opearion" 
    
    # return jsonify({"result": result})
    return str(result)