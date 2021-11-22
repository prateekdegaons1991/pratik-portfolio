from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        return redirect(url_for('home'))
    return render_template("index.html")


@app.route('/projects')
def projects():
    return render_template("projects.html")


if __name__ == "__main__":
    app.run(debug=True)
