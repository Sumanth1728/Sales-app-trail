from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateTimeField,RadioField,SelectField,TextField,TextAreaField,SubmitField,SelectMultipleField
from wtforms.validators import DataRequired,Email,EqualTo,Length


class EvaluationForm(FlaskForm):
    Approve=SubmitField("Approve")
    Decline=SubmitField("Decline")

class Selectvar(FlaskForm):
    var1=SelectField('Variable 1 (x-variable)',validators=[DataRequired()])
    var2=SelectField('Variable 2 (Y-Variable)')
    submit=SubmitField("submit")

class SelectGraph(FlaskForm):
    GraphChoice=RadioField('Select a Graph Type',validators=[DataRequired()])
    submit=SubmitField("submit")
