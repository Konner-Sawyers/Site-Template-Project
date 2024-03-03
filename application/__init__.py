from flask import Flask, render_template, jsonify, request

app = Flask(__name__, template_folder = 'templates')

@app.route('/')
def initialize():
    return render_template("index.html")

@app.route('/get_project_file', methods=['GET'])
def get_project_file():
    file_name = request.args.get('nameOfFile')
    print(file_name)
    #print("HELLO FROM PYTHON")
    file = render_template(file_name)
    return jsonify({'result': file})