from flask import Flask,render_template,redirect,url_for,request
import random

app = Flask(__name__)

todo_task = []

@app.route("/", methods=["GET","POST"])
@app.route("/home", methods=["GET","POST"])
def home():
  if request.method == "POST":
    ttask = request.form["todo"]
    if ttask != "":
      cur_id = random.randint(1,100)
      todo_task.append({
        "id" : cur_id,
        "task" : ttask,
        "checked" : False
    })
      return redirect(url_for("home"))
    else:
      return redirect(url_for("home"))
  return render_template("index.html", task=todo_task)

@app.route("/checked/<int:todo_id>", methods=["POST"])
def checked(todo_id):
  for todo in todo_task:
    if todo['id'] == todo_id:
      todo['checked'] = not todo['checked']
      break
  return redirect(url_for('home'))
  
@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete(todo_id):
  global todo_task
  for todo in todo_task:
    if todo['id'] == todo_id:
      todo_task.remove(todo)
  return redirect(url_for('home'))

if "__main__" == __name__ :
  app.run(debug=True)