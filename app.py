from flask import Flask, redirect, url_for, render_template
from dotenv import load_dotenv
from urllib.parse import quote
import requests
import os

app = Flask(__name__)
load_dotenv()

COGNITO_USER_POOL_ID = os.getenv('COGNITO_USER_POOL_ID')
COGNITO_CLIENT_ID = os.getenv('COGNITO_CLIENT_ID')
COGNITO_CLIENT_SECRET = os.getenv('COGNITO_CLIENT_SECRET')
COGNITO_DOMAIN = os.getenv('COGNITO_DOMAIN')
COGNITO_IDENTITY_POOL_ID = os.getenv('COGNITO_IDENTITY_POOL_ID')
AWS_REGION = os.getenv('AWS_REGION')
KEY_ID = os.getenv('KEY_ID')
SECRET_KEY = os.getenv('SECRET_KEY')


@app.route('/login')
def login():
    profile_url = url_for('profile', _external=True)
    redirect_uri = quote(profile_url)
    # login_url = f'{COGNITO_DOMAIN}/login?response_type=code&client_id={COGNITO_CLIENT_ID}&redirect_uri=http%3A%2F%2Flocalhost%3A5000%2Fprofile' 
    login_url = f'{COGNITO_DOMAIN}/login?response_type=code&client_id={COGNITO_CLIENT_ID}&redirect_uri={redirect_uri}'
    return redirect(login_url)


@app.route('/signup')
def signup():
    profile_url = url_for('profile', _external=True)
    redirect_uri = quote(profile_url)
    signup_url = f'{COGNITO_DOMAIN}/signup?response_type=code&client_id={COGNITO_CLIENT_ID}&redirect_uri={redirect_uri}'
    return redirect(signup_url)


@app.route('/logout')
def logout():
    index_url = url_for('index', _external=True)
    print(index_url)
    logout_uri = quote(index_url)
    print(logout_uri)

    logout_url = f'{COGNITO_DOMAIN}/logout?client_id={COGNITO_CLIENT_ID}&logout_uri={logout_uri}'
    return redirect(logout_url)


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
