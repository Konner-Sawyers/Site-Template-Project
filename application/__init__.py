from flask import Flask, render_template, jsonify, request

app = Flask(__name__, template_folder = 'templates')

programming_portfolio_dict = {
    'Python' : '<div class="tag_block"><p class="tag">Python    <span style="background-color:red;" class="dot"></span><p></div>',
    'HTML/CSS' : '<div class="tag_block"><p class="tag">HTML/CSS    <span style="background-color:lightblue;" class="dot"></span><p></div>',
    'C++' : '<div class="tag_block"><p class="tag">C++    <span style="background-color:green;" class="dot"></span><p></div>',
    'Jupyter' : '<div class="tag_block"><p class="tag">Jupyter    <span style="background-color:orange;" class="dot"></span><p></div>',
    'SQL' : '<div class="tag_block"><p class="tag">SQL    <span style="background-color:blue;" class="dot"></span><p></div>',
    'MySQL' : '<div class="tag_block"><p class="tag">MySQL    <span style="background-color:white;" class="dot"></span><p></div>',
    'Docker' : '<div class="tag_block"><p class="tag">Docker    <span style="background-color:yellow;" class="dot"></span><p></div>',
    'Numpy' : '<div class="tag_block"><p class="tag">Numpy    <span style="background-color:purple;" class="dot"></span><p></div>',
    'Tkinter' : '<div class="tag_block"><p class="tag">Tkinter    <span style="background-color:indigo;" class="dot"></span><p></div>',
    'API' : '<div class="tag_block"><p class="tag">API    <span style="background-color:magenta;" class="dot"></span><p></div>'
    #'Python' : '<div class="tag_block"><p class="tag">Jupyter    <span style="background-color:orange;" class="dot"></span><p></div>',
    #'Python' : '<div class="tag_block"><p class="tag">Jupyter    <span style="background-color:orange;" class="dot"></span><p></div>',
    #'Python' : '<div class="tag_block"><p class="tag">Jupyter    <span style="background-color:orange;" class="dot"></span><p></div>',
    #'Python' : '<div class="tag_block"><p class="tag">Jupyter    <span style="background-color:orange;" class="dot"></span><p></div>',
}

@app.route('/')
def initialize():
    variable = 'HELLO FROM FLASK'
    return render_template("index.html", variable = variable)

@app.route('/get_project_file', methods=['GET'])
def get_project_file():
    file_name = request.args.get('nameOfFile')
    file = render_template(file_name, variable = programming_portfolio_dict)
    return jsonify({'result': file})