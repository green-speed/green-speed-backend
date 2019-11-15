from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/route')
def find_bus():
    from_x = request.args.get('from_x') #if key doesn't exist, returns None
    from_y = request.args.get('from_y')
    to_x = request.args.get('to_x')
    to_y = request.args.get('to_y')
    print('from_x: ', from_x)
    print('from_y: ', from_y)
    print('to_x: ', to_x)
    print('to_y: ', to_y)
    return '''<h1>from_x: {}</h1>'''.format(from_x)


if __name__ == '__main__':
    app.run()


