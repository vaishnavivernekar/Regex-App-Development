from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    regex = request.form['regex']
    sample_text = request.form['sample_text']
    matches = re.findall(regex, sample_text)
    return render_template('results.html', matches=matches)

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form['email']
    if re.match(r'^[\w\.-]+@[\w\.-]+$', email):
        return render_template('email_validation.html', valid=True)
    else:
        return render_template('email_validation.html', valid=False)

if __name__ == '__main__':
    app.run(debug=True)
