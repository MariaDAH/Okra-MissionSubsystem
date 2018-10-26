import os
import logging
#import requests
from flask import Flask, render_template, request, redirect, session, flash, url_for, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField,FileField
from werkzeug import secure_filename


# Blueprint module to integrate fastsecret api
from api.api import api

app = Flask(__name__)

app.secret_key = 'manyrandombytes3skdjk8wjhdhd'

app.logger.setLevel(logging.INFO)

app.register_blueprint(api,url_prefix="/api")


class ReusableForm(Form):

    firstname = TextField('First Name:')
    lastname = TextField('Name:')
    email = TextField('Email:')
    confiremail = TextField('Email Confirmation:')
    username = TextField('UserName:')
    passwd= TextField('Password:')
    avatar=FileField('Avatar:')


def reset(self):
    blankData = MultiDict([ ('csrf', self.reset_csrf() ) ])
    self.process(blankData)


def write_to_file(filename,data):
    """"Handle the process of writing data to a file"""
    with open(filename,"a") as file:
        file.writelines(data)

#Retrieve job titles list to populate dropdown
def get_all_jobtitles():
    """Get all of the messages and separate by a 'br'"""
    jobtitle = []
    with open("data/jobtitles.txt", "r") as job_titles:
      jobtitles = job_titles.readlines()
    return jobtitles


##Retrieve medicalcons list to populate dropdown
def get_all_medicalcons():
    """Get all of the messages and separate by a 'br'"""
    medicalcon = []
    with open("data/medicalcons.txt", "r") as medical_cons:
      medicalcons = medical_cons.readlines()
    return medicalcons


@app.route('/')
def index():
  return render_template("index.html", page_title="Index")


@app.route('/mission', methods=["GET","POST"])
def mission():

  print("loading mission")

  form = ReusableForm(request.form)

  if request.method == "POST" and form.validate():


      # this line goes to the console/terminal in flask dev server
    print(request.form)
    # this line prints out the form to the browser
    #return jsonify(request.form.to_dict())


    firstname=form.firstname.data
    lastname=form.lastname.data
    email=form.email.data
    confiremail=form.confiremail.data
    username=form.username.data
    password=form.passwd.data
    #filename = secure_filename(form.avatar.data)
    #print(filename)
    #form.avatar.data.save('data/uploads/' + filename)
    #flash("Thanks" + firstname + " , for sign in!")
    flash('Thanks for registering')

    print("Hello################################################################", form.username.data)

    return redirect(url_for('missionstart'), username=username)

  else:

    return render_template("mission.html", page_title="Mission")


@app.route('/missionstart/<username>')
def missionstart(username):
  return render_template("missionstart.html", user = username)


@app.route('/step1')
def step1():
  jobtitles = get_all_jobtitles()
  medicalcons = get_all_medicalcons()
  return render_template("step1.html", job_titles=jobtitles, medical_cons=medicalcons)


@app.route('/fooddiary')
def fooddiary():
  #foods=[]
  #foods = api.api_foods_options()
  #return render_template("fooddiary.html", foods)
  #return render_template("fooddiary.html", page_title="Food diary")
  return redirect(url_for('api.authenticate'))



if __name__=='__main__':
  app.run(host=os.getenv('IP'),port=int(os.getenv('PORT')), debug = True)

