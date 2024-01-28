from flask import Flask,render_template
from test import app as testApp
from p1 import app as p1App
from p2 import app as p2App

app = Flask(__name__)
app.register_blueprint(testApp)
app.register_blueprint(p1App)
app.register_blueprint(p2App)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug=True)