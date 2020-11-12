#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File Name: hello.py
@Author: cmxjs
@Description: A Simple Example, start cmd: env FLASK_APP=hello.py flask run
              externally visible server: flask run -h 0.0.0.0
              get more flask run option: flask run --help

"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"
