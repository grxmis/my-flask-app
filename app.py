from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Γεια σου κόσμε από Flask στο Render!'

if __name__ == '__main__':
    app.run()
