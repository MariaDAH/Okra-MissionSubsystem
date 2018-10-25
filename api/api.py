'''from models import db, Status, Address, Business, Category, Product,Users'''
import os
import requests
from flask import Blueprint, request, jsonify, session, redirect, url_for
from fatsecret import Fatsecret


api = Blueprint('api',__name__, template_folder="api")


consumer_key = '40ca6a9cd34648fd80be50827fe46f7d'
consumer_secret = '68a259ab89e947d0b3248cd98a41d4eb'

fs = Fatsecret(consumer_key, consumer_secret)


@api.route("/")
def index():
    if request.args.get('oauth_verifier'):

        verifier_pin = request.args.get('oauth_verifier')

        # Store token as desired. The session is now authenticated
        session_token = fs.authenticate(verifier_pin)

        return redirect(url_for('profile'))

    else:
        return "<a href={0}>Authenticate Access Here</a>".format(url_for('api.authenticate'))


@api.route("/auth")
def authenticate():

    auth_url = fs.get_authorize_url(callback_url="http://127.0.0.1:5000")

    return redirect(auth_url)


@api.route("/profile")
def profile():
    food = fs.foods_get_most_eaten()

    return "<h1>Profile</h1><div><strong>Most Eaten Foods</strong><br>{}</div>"\
        .format(food)


#return all possible foods that match when filtering by name
#test0: items no found
#test1: several items found
#test3: error server response
#@api.route('/foods/options')
def api_foods_options():

    all_options =  []

    return jsonify(all_options)
