from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        if request.form.get('action') == 'hello':
            message = "Γεια σου κόσμε!"
        elif request.form.get('action') == 'goodbye':
            message = "Αντίο φίλε μου!"
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run()
