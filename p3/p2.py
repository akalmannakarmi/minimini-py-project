# WAP to perform the following
# 1) Display todo list
# 2) Able to add task
# 3) Able to remove task
# Bonus also use file handling

from os import path as PATH
from flask import Blueprint,render_template,send_file,redirect,request
app = Blueprint('p2', __name__)
todos = []

def read():
    global todos
    if PATH.exists("todo.txt"):
        with open("todo.txt","r") as f:
            todos = f.readlines()
            print(todos)

def write():
    with open("todo.txt","w") as f:
        f.writelines(todos)


@app.route("/p2/",methods=["GET"])
def showTodos():
    if not todos:
        read()
    return render_template("p2/todo.html",todos=todos)

@app.route("/p2/add",methods=["GET"])
def addTask():
    if not todos:
        read()
    task=request.args.get("task")+"\n"
    todos.append(task)
    write()
    return redirect("/p2")

@app.route("/p2/remove",methods=["GET"])
def remove():
    if not todos:
        read()
    task=request.args.get("task")+"\n"
    todos.remove(task)
    write()
    return redirect("/p2")