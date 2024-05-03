from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user database
users = {'adi': 'pwd123'}

@app.route('/')
def home():
    return 'Welcome to the Flask Login Example'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('success', username=username))
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html', error=None)

@app.route('/success/<username>')
def success(username):
    return f'Welcome, {username}!'

if __name__ == '__main__':
    app.run(debug=True)
