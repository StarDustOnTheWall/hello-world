from sanic import Sanic
from sanic.response import json
from admin import homepage
app = Sanic('test')
app.blueprint(homepage)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=15020)