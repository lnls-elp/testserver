#!/usr/bin/env python3

from flask import Flask

app = flask(__name__)

@app.route('/')
def index():
    return "Hello Sirius"

if __name__ == "__main__":
    app.run()
