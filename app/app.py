from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        return f"Thanks {name}, your feedback is submitted!"
    return render_template('form.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
