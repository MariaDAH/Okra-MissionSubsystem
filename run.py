import os
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
  return render_template("index.html", page_title="Index")


@app.route('/mission')
def mission():
  return render_template("mission.html", page_title="Mission")


@app.route('/missionstart')
def missionstart():
  return render_template("missionstart.html", page_title="Mission Start")

@app.route('/step1')
def step1():
  return render_template("step1.html", page_title="Getting ready")

if __name__=='__main__':
  app.run(host=os.getenv('IP'),port=int(os.getenv('PORT')), debug = True)

