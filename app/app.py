from flask import Flask, render_template, request
app = Flask(_name_)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        return f"Thanks {name}, your feedback is submitted!"
    return render_template('form.html')

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
