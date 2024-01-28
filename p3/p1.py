# WAP to perform the following
# 1) Subjects page with atleast 2 subjects which are clickable and take to that subjects page
# 2) Each subjects page must contain a header description and a link to download its files

from flask import Blueprint,render_template,send_file
app = Blueprint('p1', __name__)

@app.route("/p1/",methods=["GET"])
def subjects():
    return render_template("p1/subjects.html")

@app.route("/p1/math",methods=["GET"])
def math():
    return render_template("p1/math.html")

@app.route("/p1/science",methods=["GET"])
def science():
    return render_template("p1/science.html")

@app.route("/p1/files/<file>",methods=["GET"])
def files(file):
    if file!="science" and file!="math":
        return "File Not allowed"
    return send_file(f"static/p1/docs/{file}.docx")
