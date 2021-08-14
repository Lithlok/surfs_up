from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'


# Skill drill
# @app.route('/')
# def answer_to(): #everything
#     return '42'
