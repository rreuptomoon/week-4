
from unicodedata import name
from unittest import result
from flask import Flask,  redirect, url_for
from flask import request
from flask import session
from flask import render_template
app=Flask(__name__ , static_folder="public",static_url_path="/")
app.secret_key="test your page!"





@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signin", methods=["POST"])
def signin():
    name=request.form["name"]   # get the form name & password
    password=request.form["password"] 
    if name =="test" and password =="test":  # if  filter the name &password
        session["name"]= name
        return redirect(url_for("member"))
    else:
        return redirect(url_for("error",name=name,password=password))
        #pass the name=name,password=password to error page

@app.route("/member")
def member():
    if request.method=="GET":   #get method judge have session id or not
        sId=session.get("name",None)
        if not sId:
            return redirect(url_for("home"))
    if request.method=="POST":      #post method  
        sId = session.get("name",None)
        if not sId:
            return redirect(url_for("home")) # if not to home 
    else:
        return render_template("member.html")


@app.route("/logout")    # set the logout to home.page
def logout():
        session.pop("name",None)
        return redirect(url_for("home"))


@app.route("/error") # receive the name &password and show the query string
def error():
    name=request.args.get("name")
    password=request.args.get("password")
    mystring=""
    if name== "" or password == "":          
        #name or password empty
        return render_template("error.html",mystring="Please Entry Your Name & Password!!")
    else:
        return render_template("error.html",mystring="You got Wrong Entry, Please try again!")
   
       

app.run(port=3000)