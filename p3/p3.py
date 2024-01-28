# WAP to perform the following
# 1) Sign up 
# 2) Login with session
# 3) logout
# Bonus also use file handling

from os import path as PATH
from flask import Blueprint,render_template,redirect,request,session
app = Blueprint('p3', __name__)

@app.route("/p3/",methods="GET")
def index():
    if 'username' not in session:
        return render_template('p2/index.html',session=session)


@app.route('/p3/signup', methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template('signup.html',rData={})
    
    data = request.form.deepcopy()
    username = request.form['username']

    username=data['username']
    email=data['email']
    password=data['0password']
    # store some place

    return redirect('/login')

@app.route('/p3/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html',rData={})
    
    data = request.form.deepcopy()
    print(data)
    rq=['email','0password']
    if any(i not in data for i in rq):
        result = f"Require:{','.join(rq)}"
        return render_template('login.html',error=result)
    
    # find user with that email
    
    # check password
    if True:
        session['username'] = "insert username"
        return redirect('/p3/')
    
    return render_template('login.html', rData=data,error="Invalid username or password")

@app.route('/logout', methods=["GET","POST"])
def logout():
    session.clear()
    return redirect('/login')