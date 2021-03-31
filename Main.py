
from flask import Flask, render_template, session, redirect, url_for, session,flash,request
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,
                     TextAreaField,SubmitField)
from wtforms.validators import DataRequired
from datetime import datetime
from basecong import app,mail
from flask_mail import *
from forms import Selectvar,SelectGraph
import os
from dataviz import np,pd,plt,sns,dataviz
# Now create a WTForm Class
# Lots of fields available:
# http://wtforms.readthedocs.io/en/stable/fields.html

ALLOWED_EXTENSIONS = {'txt', 'xlsx','csv'}
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
            global grp
            grp=dataviz(path)
            return redirect(url_for("SelectGraphFields"))

            #return redirect(url_for("datavizu"))

        else:
            flash("extension Not allowed")


    return render_template('index.html')




@app.route('/SelectGraphFields/', methods=['GET', 'POST'])
def SelectGraphFields():
    headers=list(grp.headers())
    list1=list()
    for i in headers:
        k=(i,i)
        list1.append(k)
    list2=list1.copy()
    list2.insert(0,("None","None"))
    form=Selectvar()
    form.var1.choices=list1
    form.var2.choices=list2
    if form.validate_on_submit():
        var1=form.var1.data
        var2=form.var2.data
        return redirect(url_for("GraphOptions",var1=var1,var2=var2))

    return render_template('datavizheaders.html',headers=headers,form=form)


@app.route('/GraphOptions/<var1>&<var2>', methods=['GET', 'POST'])
def GraphOptions(var1,var2):
    form=SelectGraph()
    opts=GraphList(var1,var2)
    print("----------------------------------")
    print(opts)
    print("--------------------------------------")
    form.GraphChoice.choices=opts
    if form.validate_on_submit():
        Graphchoice=form.GraphChoice.data
        return redirect(url_for("GraphVisualization",var1=var1,var2=var2,Graphchoice=Graphchoice))


    return render_template('GraphOptions.html',form=form)


@app.route('/GraphVisualization/<var1>&<var2>&<Graphchoice>', methods=['GET', 'POST'])
def GraphVisualization(var1,var2,Graphchoice):
    n=DrawGraph(var1,var2,Graphchoice)


    return render_template('graph.html',n=str(n))

def GraphList(var1,var2):
    if(var2=="None"):
        try:
            a=int(grp.DataCat(var1))
            n=[("LineChart","LineChart"),("AreaChart","AreaChart")]
        except Exception as e:
            n=[("BarChart","BarChart"),("DonutChart","DonutChart")]
    else:
        try:
            a=int(grp.DataCat(var1))
            try:
                a=int(grp.DataCat(var2))
                n=[("None","no graphs Availble for this combination")]

            except Exception as e:
                n=[("None","no graphs Availble for this combination")]
        except Exception as e:
            try:
                a=int(grp.DataCat(var2))
                n=[("None","no graphs Availble for this combination")]

            except Exception as e:
                n=[("None","no graphs Availble for this combination")]

    return n

def DrawGraph(var1,var2,Graphchoice):
    if(Graphchoice=="LineChart"):
        n=grp.linechart(var1)
    elif(Graphchoice=="BarChart"):
        n=grp.barchart(var1)
    elif(Graphchoice=="AreaChart"):
        n=grp.areachart(var1)
    elif(Graphchoice=="ScatterPlot"):
        n=grp.scatterplot(var1,var2)
    elif(Graphchoice=="HexPlot"):
        n=grp.hexplot(var1,var2)
    else:
        n=0
    return n



if __name__ == '__main__':
    app.run(debug=True)
