from flask import Flask, render_template, request, redirect, url_for

 

app = Flask(__name__)

 

# A simple user database (for demonstration purposes)

users = {

    'username': 'password'

}

 

@app.route('/')

def home():

    return render_template('login.html')

 

@app.route('/login', methods=['POST'])

def login():

    username = request.form['username']

    password = request.form['password']

 

    if username in users and users[username] == password:

        return 'Login successful'

    else:

        return 'Login failed. Please check your username and password.'

 

if __name__ == '__main__':

    app.run(debug=True)