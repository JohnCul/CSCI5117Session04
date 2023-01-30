from flask import Flask, request, render_template
import os
from dotenv import load_dotenv

load_dotenv()
my_id = os.getenv("ID")
my_secret_key = os.getenv("SECRET_KEY")

print(my_id, ", ", my_secret_key)

app = Flask(__name__)

## app.rout returns a function when "/" is called in the url, returns hello_world

@app.route('/', methods=['GET'])
def hi():
  user_name = request.args.get("userName", "unknown")
  return render_template('main2.html', user=user_name) 

@app.route('/form', methods=['GET', 'POST'])
def form():
  correctness = ""
  curr_name = "Not_Mario"
  if request.method == 'POST':
    form_data = request.form
    curr_name = form_data["name"]
    print(form_data)
    if(form_data["name"] == "Rosalina"):
      correctness = "Correct"
    else:
      correctness = "False"
  return render_template('form.html', curr_name = curr_name, correctness = correctness) 