
from ast import arg
from pdb import post_mortem
from flask import Flask,  redirect, url_for
from flask import request
from flask import session
from flask import render_template
app=Flask(__name__ , static_folder="public",static_url_path="/")
app.secret_key="test you page!"

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signin", methods=["POST"])
def signin():
    name=request.form["name"]   # get the form name & password
    password=request.form["password"] 
    if name =="test" and password =="test":  # if  filter the name &password
        session["name"]= name
        return redirect(url_for("member"))
    elif name == "" or password == "":          #name or password empty
        return redirect(url_for("error",mystring="Please Entry Your Name & Password!! "))
    else:
        return redirect(url_for("error",mystring="You got Wrong Entry, Please try again!"))

        #pass the string to error page

@app.route("/member",methods=["POST","GET"])
def member():
    if "name" in session:       # set up the session 
        name=session["name"]
        session.pop("name",None)    # prevent /member with out password entry
        return render_template("member.html")
    else:
        return render_template("index.html")

@app.route("/logout",methods=["POST","GET"])    # set the logout to index.page
def logout():
        session.pop("name",None)
        return redirect(url_for("index"))


@app.route("/error/<string:mystring>") # receive the string and display to page
def error(mystring):
    return render_template("error.html",mystring=mystring)

    
app.run(port=3000)