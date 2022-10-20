#!/usr/bin/env python3
'''flak app'''
from flask import Flask, render_template, request
from flask_babel import Babel
app = Flask(__name__)

babel = Babel(app)


class Config(object):
    '''config class'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    '''determine the best match with our supported languages'''
    if 'locale' in request.args:
        locale = request.args.get('locale')
        if locale and locale in Config.LANGUAGES:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def welcome():
    '''web page rendering'''
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
