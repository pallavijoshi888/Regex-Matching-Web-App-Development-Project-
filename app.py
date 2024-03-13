from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    match_results = None
    email_validation_result = None
    if request.method == 'POST':
        if 'test_string' in request.form and 'regex' in request.form:
            # Handle regex matching
            test_string = request.form['test_string']
            regex_pattern = request.form['regex']
            match_results = re.findall(regex_pattern, test_string)
        elif 'email' in request.form:
            # Handle email validation
            email = request.form['email']
            regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            email_validation_result = re.match(regex, email) is not None
    return render_template('index.html', matches=match_results, valid=email_validation_result, email=request.form.get('email'))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
