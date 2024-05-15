from flask import Flask,render_template

app = Flask(__name__)

@app.route('/info/')
@app.route('/info/<name>')
def hello(name=None):
    return render_template('info.html', name=name)

if __name__ =="__main__":
    app.run()