from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():          #http://127.0.0.1:5000 ---> displays 'Hello World!'
    return 'Hello World!'

@app.route('/dojo')
def dojo():                 # http://127.0.0.1:5000/dojo ---> displays 'Dojo!'
    return 'Dojo!'

@app.route('/say/flask')
def say_flask():           # http://127.0.0.1:5000/say/flask ---> displays 'Hi Flask!'
    return 'Hi Flask!'

@app.route('/say/michael')
def say_michael():          #http://127.0.0.1:5000/say/michael ---> displays 'Hi Michael!'
    return 'Hi Michael!'

@app.route('/say/john')
def say_john():             #http://127.0.0.1:5000/say/john ---> displays 'Hi John!'
    return 'Hi John!'

@app.route('/repeat/<int:num>/<hello>')
def repeat_hello(hello, num):           #http://127.0.0.1:5000/repeat/35/hello ---> displays 'Hello' a set numbers of times as defined in url
    return f"{hello * num}"

@app.route('/repeat/<int:num>/<bye>')
def repeat_bye(bye, num):               ##http://127.0.0.1:5000/repeat/80/bye ---> displays 'Bye' a set numbers of times as defined in url
    return f"{bye * num}"

@app.route('/repeat/<int:num>/<dogs>')
def repeat_dogs(dogs, num):               ##http://127.0.0.1:5000/repeat/80/bye ---> displays 'Bye' a set numbers of times as defined in url
    return f"{dogs * num}"

if __name__=="__main__":
    app.run(debug=True)

