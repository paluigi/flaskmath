from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Flask Math APIs</h1><p>This site is a prototype API for math functions.</p>"


@app.route('/add', methods=['POST'])
def add():
    return "<h1>Flask Math APIs</h1><p>This site is a prototype API for math functions.</p>"


app.run()
