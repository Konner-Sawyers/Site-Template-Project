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
    'API' : '<div class="tag_block"><p class="tag">API    <span style="background-color:magenta;" class="dot"></span><p></div>',
    'Sass' : '<div class="tag_block"><p class="tag">Sass    <span style="background-color:lightgreen;" class="dot"></span><p></div>',
    #'Python' : '<div class="tag_block"><p class="tag">Jupyter    <span style="background-color:orange;" class="dot"></span><p></div>',
    #'Python' : '<div class="tag_block"><p class="tag">Jupyter    <span style="background-color:orange;" class="dot"></span><p></div>',
    #'Python' : '<div class="tag_block"><p class="tag">Jupyter    <span style="background-color:orange;" class="dot"></span><p></div>',
    #'Python' : '<div class="tag_block"><p class="tag">Jupyter    <span style="background-color:orange;" class="dot"></span><p></div>',
    'Sass' : '<div class="tag_block"><p class="tag">Sass    <span class="dot"></span><p></div>'
}



@app.route('/')
def initialize():
    return render_template("index.html")

@app.route('/home',methods = ['GET', 'POST'])
def home():
    return render_template("home_page.html")

@app.route('/about',methods = ['GET', 'POST'])
def about():
    return render_template("about_page.html")

@app.route('/contact',methods = ['GET', 'POST'])
def contact():
    return render_template("contact_page.html")

@app.route('/projects',methods = ['GET', 'POST'])
def projects():
    return render_template("project_page.html")

@app.route('/get_project_file', methods=['GET'])
def get_project_file():
    file_name = request.args.get('nameOfFile')
    file = render_template(file_name, variable = programming_portfolio_dict)
    return jsonify({'result': file})