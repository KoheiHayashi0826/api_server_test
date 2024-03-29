from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!!!!"

@app.route('/hello', methods=['POST'])
def hello():
    if request.method=='POST':
        name = request.form['name']
    else:
        name = 'no name.'
    return render_template('hello.html', title='flask test', name=name)

if __name__ == "__main__":
    app.run(debug=True)