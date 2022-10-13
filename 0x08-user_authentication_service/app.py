#!/usr/bin/env python3
'''flak app'''
from auth import Auth
from flask import Flask, jsonify, request, abort
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/')
def message():
    '''return a greeting message'''
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users() -> str:
    '''Register user'''
    try:
        email = request.form['email']
        password = request.form['password']
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    if AUTH.valid_login(email, password) is False:
        abort(401)
    else:
        session_id = AUTH.create_session(email)
        resp = jsonify({"email": "<user email>", "message": "logged in"})
        resp.set_cookie("session_id", session_id)
        return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
