from flask import Flask, Response
from chat.db import get_stuff


app = Flask(__name__)

@app.route('/')
def hello_world():

    res = get_stuff()

    return Response(res)

if __name__ == '__main__':
    app.run()
