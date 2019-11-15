import os

from flask import Flask, jsonify, abort
from flask import request

app = Flask(__name__)

current_script_location = os.path.realpath(__file__)
root_package_dir = os.path.dirname(current_script_location)


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


@app.route('/api/v1/directions')
def get_directions():
    from_location = request.args.get('from') #if key doesn't exist, returns None
    to_location = request.args.get('to')
    if from_location or to_location:
        with open(os.path.join(root_package_dir, 'sample_transportaion_options.json'), 'r') as f:
            s = f.read()
        return jsonify(s)
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)


