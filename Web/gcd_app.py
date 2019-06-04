#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import flask
from flask import Flask, request

app = Flask(__name__, root_path='.',  static_folder="static", static_url_path="")


@app.route('/')
def root():
    return flask.render_template(
        'index.html'
    )


@app.route('/gcd', methods = ['GET'])
def gcd():
    if request.method == 'GET':
        a = request.args.get('num1')
        b = request.args.get('num2')
    elif request.method == 'POST':
        name_param = request.form.get('num1','num2')

    if a == None:
        a = 0
    if b == None:
        b = 0

    a = int(a)
    b = int(b)
	
    def NOD(a,b):
        if (b==0):
            return a
        else: 
            return int(NOD(b, a % b))

    result = NOD(a, b)


    return flask.render_template(
        'gcd.html',
        result = result,
        a=a,
        b=b,
        method=request.method
    )

if __name__ == '__main__':
   app.run(debug = True)
