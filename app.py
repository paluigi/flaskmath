from flask import Flask, request, jsonify, make_response, abort, render_template
from datetime import datetime

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("home.html", date_time=date_time)
    #return "<h1>Flask Math APIs</h1><p>This site is a prototype API for math functions.</p>"


@app.route('/add', methods=['POST'])
def add():
    """
    Receive a JSON with two items:
    - x : numeric
    - y : numeric
    Returns json with result: x+y
    Example:
    >>> test = requests.post("http://127.0.0.1:5000/add", json={"x":5, "y":"9"})
    >>> test.text
    '{\n  "result": 14.0\n}\n'
    """
    if not request.json:
        abort(400)
    try:
        res = float(request.json["x"]) + float(request.json["y"])
    except (ValueError, KeyError) as e:
        return make_response(jsonify({'error': f'wrong input - {e}'}), 400)
    return make_response(jsonify({"result": res}), 200)


@app.route('/addmany', methods=['POST'])
def addmany():
    """
    Receive a JSON with one item:
    - x : list of numbers, comma separated
    Returns json with result: sum of all numbers in x
    Example:
    >>> test = requests.post("http://127.0.0.1:5000/addmany", json={"x":[5,4,2]})
    >>> test.text
    '{\n  "result": 11.0\n}\n'
    """
    if not request.json:
        abort(400)
    try:
        res = 0
        for n in request.json["x"]:
            res += float(n)
    except (ValueError, KeyError) as e:
        return make_response(jsonify({'error': f'wrong input - {e}'}), 400)
    return make_response(jsonify({"result": res}), 200)


@app.route('/subtract', methods=['POST'])
def subtract():
    """
    Receive a JSON with two items:
    - x : numeric
    - y : numeric
    Returns json with result: x-y
    Example:
    >>> test = requests.post("http://127.0.0.1:5000/subtract", json={"x":5, "y":"9"})
    >>> test.text
    '{\n  "result": -4.0\n}\n'
    """
    if not request.json:
        abort(400)
    try:
        res = float(request.json["x"]) - float(request.json["y"])
    except (ValueError, KeyError) as e:
        return make_response(jsonify({'error': f'wrong input - {e}'}), 400)
    return make_response(jsonify({"result": res}), 200)


@app.route('/multiply', methods=['POST'])
def multiply():
    """
    Receive a JSON with two items:
    - x : numeric
    - y : numeric
    Returns json with result: x*y
    Example:
    >>> test = requests.post("http://127.0.0.1:5000/multiply", json={"x":5, "y":"9"})
    >>> test.text
    '{\n  "result": 45.0\n}\n'
    """
    if not request.json:
        abort(400)
    try:
        res = float(request.json["x"]) * float(request.json["y"])
    except (ValueError, KeyError) as e:
        return make_response(jsonify({'error': f'wrong input - {e}'}), 400)
    return make_response(jsonify({"result": res}), 200)


@app.route('/divide', methods=['POST'])
def divide():
    """
    Receive a JSON with two items:
    - x : numeric
    - y : numeric
    Returns json with result: x/y
    Example:
    >>> test = requests.post("http://127.0.0.1:5000/divide", json={"x":5, "y":"9"})
    >>> test.text
    '{\n  "result": 0.5555555555555556\n}\n'
    """
    if not request.json:
        abort(400)
    try:
        res = float(request.json["x"]) / float(request.json["y"])
    except (ValueError, KeyError) as e:
        return make_response(jsonify({'error': f'wrong input - {e}'}), 400)
    return make_response(jsonify({"result": res}), 200)


@app.route('/floor_division', methods=['POST'])
def floor_division():
    """
    Receive a JSON with two items:
    - x : numeric
    - y : numeric
    Returns json with result: x//y
    Example:
    >>> test = requests.post("http://127.0.0.1:5000/floor_division", json={"x":35, "y":"9"})
    >>> test.text
    '{\n  "result": 3.0\n}\n'
    """
    if not request.json:
        abort(400)
    try:
        res = float(request.json["x"]) // float(request.json["y"])
    except (ValueError, KeyError) as e:
        return make_response(jsonify({'error': f'wrong input - {e}'}), 400)
    return make_response(jsonify({"result": res}), 200)


@app.route('/remainder', methods=['POST'])
def remainder():
    """
    Receive a JSON with two items:
    - x : numeric
    - y : numeric
    Returns json with result: x%y
    Example:
    >>> test = requests.post("http://127.0.0.1:5000/remainder", json={"x":35, "y":"9"})
    >>> test.text
    '{\n  "result": 8.0\n}\n'
    """
    if not request.json:
        abort(400)
    try:
        res = float(request.json["x"]) % float(request.json["y"])
    except (ValueError, KeyError) as e:
        return make_response(jsonify({'error': f'wrong input - {e}'}), 400)
    return make_response(jsonify({"result": res}), 200)


@app.route('/nroot', methods=['POST'])
def nroot():
    """
    Receive a JSON with two items:
    - x : numeric
    - y : numeric
    Returns json with result: y-th root of x
    Example:
    >>> test = requests.post("http://127.0.0.1:5000/nroot", json={"x":16, "y":"2"})
    >>> test.text
    '{\n  "result": 4.0\n}\n'
    """
    if not request.json:
        abort(400)
    try:
        res = float(request.json["x"]) ** (1 / float(request.json["y"]))
    except (ValueError, KeyError) as e:
        return make_response(jsonify({'error': f'wrong input - {e}'}), 400)
    return make_response(jsonify({"result": res}), 200)


@app.route('/power', methods=['POST'])
def power():
    """
    Receive a JSON with two items:
    - x : numeric
    - y : numeric
    Returns json with result: y-th power of x
    Example:
    >>> test = requests.post("http://127.0.0.1:5000/power", json={"x":16, "y":"2"})
    >>> test.text
    '{\n  "result": 256.0\n}\n'
    """
    if not request.json:
        abort(400)
    try:
        res = float(request.json["x"]) ** float(request.json["y"])
    except (ValueError, KeyError) as e:
        return make_response(jsonify({'error': f'wrong input - {e}'}), 400)
    return make_response(jsonify({"result": res}), 200)


@app.errorhandler(404)
def not_found(error):
    """
    Handle page not found returning a JSON
    """
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run()
