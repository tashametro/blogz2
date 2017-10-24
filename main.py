from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = '
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blogger(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    Blogger = db.Column(db.String(100))
    a_new_post = db.Column(db.Boolean)

    def __init__(self, Blogger):
        self.Blogger = Blogger
        self.a_new_post = False


