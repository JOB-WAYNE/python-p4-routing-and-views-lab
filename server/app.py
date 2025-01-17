#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string>')
def print_string(string):
    print(string)  # Prints to console
    return string  # Displays in browser

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = range(parameter + 1)
    return '<br>'.join(str(num) for num in numbers)

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    try:
        result = None
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == 'div':
            result = num1 / num2
        elif operation == '%':
            result = num1 % num2
        else:
            return f'Invalid operation: {operation}'
        
        return f'{num1} {operation} {num2} = {result}'
    except ZeroDivisionError:
        return 'Error: Division by zero'
    except Exception as e:
        return f'Error: {str(e)}'



if __name__ == '__main__':
    app.run(port=5555, debug=True)
