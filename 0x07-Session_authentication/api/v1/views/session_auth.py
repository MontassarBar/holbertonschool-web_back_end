#!/usr/bin/env python3
'''handles all routes for the Session authentication'''

from api.v1.views import app_views
from flask import jsonify, request
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    '''login'''
    email = request.form.get('email')
    pwd = request.form.get('password')
    if email is None or not email:
        return jsonify({"error": "email missing"}), 400
    if pwd is None or not pwd:
        return jsonify({"error": "password missing"}), 400
    user = User()
    x = user.search({"email": email})
    if len(x) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    for u in x:
        if u.is_valid_password(pwd) is True:
            from api.v1.app import auth
            Session_ID = auth.create_session(u.id)
            uj = jsonify(u.to_json())
            uj.set_cookie(os.getenv("SESSION_NAME"), Session_ID)
            return uj
        else:
            return jsonify({"error": "wrong password"}), 401
