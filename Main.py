
from flask import Flask, render_template, session, redirect, url_for, session,flash,request
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,
                     TextAreaField,SubmitField)
from wtforms.validators import DataRequired
from tables import db, B_Admin ,B_Employee ,B_Customer,B_Customer_transactions,B_Customer_Card_Details,CardRequests,logs,CardDeActLogs
from datetime import datetime
from basecong import app,mail
from flask_mail import *
from forms import createcustomer,searchform,EditEmployee,createemloyee,RequestCards,AmountTransferForm,EvaluationForm
import os
from dataviz import np,pd,plt,sns,dataviz
# Now create a WTForm Class
# Lots of fields available:
# http://wtforms.readthedocs.io/en/stable/fields.html

ALLOWED_EXTENSIONS = {'txt', 'png', 'jpg', 'jpeg', 'xlsx'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            path=os.path.join("static", file.filename)
            file.save(path)
            flash("file Uploaded Succesfully")
            grp=dataviz(path)
            a="Category"
            grp.his(a)
            headers=list(grp.headers())
            print("--------------------------------------------------------")
            print(headers)
            print("--------------------------------------------------------")

            return redirect(url_for("datavizu",headers=headers))
            #return redirect(url_for("datavizu"))
        else:
            flash("extension Not allowed")


    return render_template('index.html')




@app.route('/datavizu/<headers>', methods=['GET', 'POST'])
def datavizu(headers):
    return render_template('datavizheaders.html',headers=list(headers))




if __name__ == '__main__':
    app.run(debug=True)
