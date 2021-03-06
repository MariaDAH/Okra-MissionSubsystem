import os
import logging
#import requests
from flask import Flask, render_template, request, redirect, session, flash, url_for, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField,FileField, SelectField,FormField,BooleanField
from werkzeug.utils import secure_filename
from flask_wtf.file import FileField
from werkzeug import SharedDataMiddleware


# Blueprint module to integrate fastsecret api
from api.api import api


UPLOAD_FOLDER = '/data/uploads'

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

app.secret_key = 'manyrandombytes3skdjk8wjhdhd'

app.logger.setLevel(logging.INFO)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.add_url_rule('/data/uploads/<filename>', 'uploaded_file',build_only=True)

app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
    '/data/uploads':  app.config['UPLOAD_FOLDER']
})

app.register_blueprint(api,url_prefix="/api")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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


class UploadFileForm(Form):

    image = FileField(u'Image File')
    description  = TextAreaField(u'Image Description')



class SignUpForm(Form):

    #firstname = TextField('First Name:',[validators.required(), validators.length(max=30)])
    #lastname = TextField('Name:',[validators.required(), validators.length(max=30)])
    #email = TextField('Email:',[validators.required(), validators.length(max=60)])
    #confiremail = TextField('Email Confirmation:',[validators.required(), validators.length(max=60)])
    #username = TextField('UserName:',[validators.required(), validators.length(max=30)])
    #passwd= TextField('Password:',[validators.required(), validators.length(max=15)])
    #confpwd = TextField('Confirm Password:',[validators.required(), validators.length(max=15)])
    #uploadFileForm=FormField(UploadFileForm, [validators.regexp(u'.')])
    #terms=BooleanField()

    firstname = TextField('First Name:')
    lastname = TextField('Name:')
    email = TextField('Email:')
    confiremail = TextField('Email Confirmation:')
    username = TextField('UserName:')
    passwd= TextField('Password:')
    confpwd = TextField('Confirm Password:')
    uploadFileForm=FormField(UploadFileForm, [validators.regexp(u'.')])
    terms=BooleanField()


class Step1Form(Form):

    jobtitles = get_all_jobtitles()
    medicalcons = get_all_medicalcons()
    jobtitle = SelectField(label='jobId', choices=jobtitles)
    medicalcon = SelectField(label='medicalConditionId', choices=medicalcons)
    height = TextField('Height:')
    weight = TextField('Weight:')
    age = TextField('Age:')


def reset(self):
    blankData = MultiDict([ ('csrf', self.reset_csrf() ) ])
    self.process(blankData)


def write_to_file(filename,data):
    """"Handle the process of writing data to a file"""
    with open(filename,"a") as file:
        file.writelines(data)


@app.route('/')
def index():
  return render_template("index.html", page_title="Index")


'''def upload_file():
    print('I am i signuppnl')
    if request.method == 'POST':
        print('I am i signuppnl')
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return'''




@app.route('/mission', methods=["GET","POST"])
def mission():

  form = SignUpForm(request.form)

  print(request.form)
  if request.method == "POST" and form.validate():
    #this line prints out the form to the browser
    #return jsonify(request.form.to_dict())
    firstname=form.firstname.data
    lastname=form.lastname.data
    email=form.email.data
    confiremail=form.confiremail.data
    username=form.username.data
    password=form.passwd.data
    #filename = secure_filename(form.image.filename)
    #form.file.data.save('/data/uploads/' + filename)
    #flash("Thanks" + firstname + " , for sign in!")
    #flash('Thanks for registering')
    return redirect(url_for('missionstart', user=username))

  return render_template("mission.html", page_title="Mission")


@app.route('/missionstart/<user>')
def missionstart(user):
  return render_template("missionstart.html", username = user)


@app.route('/step1')
def step1():
  jobtitles = get_all_jobtitles()
  medicalcons = get_all_medicalcons()
  step1form = Step1Form(request.form)
  print("I am here")
  print(request.method)
  if request.method == "POST" and step1form.validate():
    print(request.method)
    jobtitle = step1form.jobId.data
    medicalcon = step1form.madicalConditionId.data
    height = step1form.height.data
    weight = step1form.weight.data
    age = step1form.age.data
    print(jobtitle +" " + medicalcon + " " + height + " " + weight + " " + " " + age)
    return redirect(url_for('fooddiary'))
  return render_template("step1.html", job_titles=jobtitles, medical_cons=medicalcons)


@app.route('/fooddiary')
def fooddiary():
  #foods=[]
  #foods = api.api_foods_options()
  #return render_template("fooddiary.html", foods)
  #return render_template("fooddiary.html", page_title="Food diary")
  return redirect(url_for('api.index'))



if __name__=='__main__':
  app.run(host=os.getenv('IP'),port=int(os.getenv('PORT')), debug = True)

