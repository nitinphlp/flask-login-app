from flask import Flask
application = Flask(__name__)

@application.route('/')
def login_page():
    return 'This is login page!'