from urllib import response
from flask import Flask, render_template, redirect, url_for, request, abort
import requests


app = Flask(__name__)


SITE_KEY = '6LfTZOEpAAAAAP7-jbc8ekdfmC0ULAI2I5od8cCK'
SECRET_KEY = '6LfTZOEpAAAAACjh_6EbAV13_1mHtr_7tUOPF6H'
VERIFY_URL = 'https://www.google.com/recaptcha/api/siteverify'


@app.route("/", methods=['GET'])
def home():
    return render_template('home.html', site_key=SITE_KEY)


@app.route("/sign-user-up", methods=['POST'])
def sign_up_user():
    secret_response = request.form['g-recaptcha-response']

    verify_response = requests.post(url=f'{VERIFY_URL}?secret={SECRET_KEY}&response={secret_response}').json()

    if verify_response['success'] == False or verify_response['score'] < 0.5:
        abort(401)

    return redirect(url_for('home'))


if __name__=='__main__':
    app.run(debug=True)