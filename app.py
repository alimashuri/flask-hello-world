# -*- coding: utf-8 -*-

"""
    My First Python App
"""

import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
        render_template, flash



# create our little application :)
app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DEBUG=True
))

app.config.from_envvar('ALIMASHURI_ENV', silent=True)

@app.route('/')
def index():
    return render_template('index.html', entries="")


if __name__ == '__main__':
    app.run()


