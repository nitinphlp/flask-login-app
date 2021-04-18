from flask import Flask, render_template, request
application = Flask(__name__)

credential_dict = {'nitin':'abcd', 'guest':'1234'}


@application.route('/')
def init_login_page():
    return render_template("login.html")


@application.route('/form_login', methods=['POST','GET'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username not in credential_dict.keys():
        return render_template('login.html',info='Login failed due to incorrect username and password!')
    elif credential_dict[username] != password:
        return render_template('login.html',info='Login failed due to incorrect username and password!')
    else:
        return render_template('welcome.html', name=username)


if __name__ == '__main__':
    application.run()