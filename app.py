from flask import Flask, render_template

app = Flask(__name__)

'''
safe - 
capitalize
lower
upper
title
trim
striptags
'''

@app.route('/')
#def index():
#    return "<h1>Hello World$ ... </h1>"
def index():
    stuff = "I want to it be <strong>bold</strong>"
    gyumolcsok = ["alma", "korte", 41]
    return render_template("index.html", stuff=stuff, gyumolcsok=gyumolcsok)

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)

#--
app.run(host='0.0.0.0', port=5000, debug=True)