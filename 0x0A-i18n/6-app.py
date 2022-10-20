#!/usr/bin/env python3
'''flak app'''
from flask import Flask, render_template, request, g
from flask_babel import Babel
app = Flask(__name__)

babel = Babel(app)


class Config(object):
    '''config class'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    '''determine the best match with our supported languages'''
    if 'locale' in request.args:
        locale = request.args.get('locale')
        if locale and locale in Config.LANGUAGES:
            return locale
        if g.user:
            if g.user['locale'] in Config.LANGUAGES:
                return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    '''returns a user dictionary'''
    if 'login_as' in request.args:
        id = request.args.get('login_as')
        if id and int(id) in users.keys():
            return users[int(id)]
    return None


@app.before_request
def before_request():
    '''find a user if any, and set it as a global on flask.g.user'''
    user = get_user()
    g.user = user


@app.route('/')
def welcome():
    '''web page rendering'''
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
