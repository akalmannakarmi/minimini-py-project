from flask import Blueprint,render_template,request
app = Blueprint('test', __name__)

@app.route("/test/",methods=["GET","POST"])
def test1():
    if request.method == "GET":
        return render_template("test.html",todos=todo)
    
    sth = request.form["sth"]

    return sth





