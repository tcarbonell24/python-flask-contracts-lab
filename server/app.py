#!/usr/bin/env python3
from flask import Flask, make_response

app = Flask(__name__)

# Mock data
contracts = {
    1: "This contract is for John and building a shed"
}

customers = ["bob"]

# Contract route
@app.route('/contract/<int:id>')
def contract(id):
    if id in contracts:
        # Return text and 200 OK
        return make_response(contracts[id], 200)
    else:
        # Return 404 Not Found
        return make_response("Contract not found", 404)

# Customer route
@app.route('/customer/<string:customer_name>')
def customer(customer_name):
    if customer_name in customers:
        # Return empty body and 204 No Content
        return make_response("", 204)
    else:
        # Return 404 Not Found
        return make_response("Customer not found", 404)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
