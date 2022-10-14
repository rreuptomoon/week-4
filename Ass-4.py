from unittest import result
from flask import Flask,  redirect, url_for
from flask import request
from flask import session
from flask import render_template
import cmath
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
    elif name== "" or password == "":          
        #name or password empty
        empty="Please Entry Your Name & Password!!"
        return redirect(url_for("error",empty=empty))
    else:
        wrong_entry="You Got Wrong Entry,Please Try Again!"
        return redirect(url_for("error",wrong_entry=wrong_entry))
        #pass the name=name,password=password to error page

@app.route("/member")
def member():
    sId=session.get("name",None)
     #get method judge have session id or not 
    if not sId:
            return redirect(url_for("home"))
    else:
        return render_template("member.html")


@app.route("/logout")    # set the logout to home.page
def logout():
        session.pop("name",None)
        return redirect(url_for("home"))

@app.route("/error") # receive the name &password and show the query string
def error():
    empty=request.args.get("empty")
    wrong_entry=request.args.get("wrong_entry")
    if empty:          
        #name or password empty
        return render_template("error.html",empty=empty)
    else:
        return render_template("error.html",wrong_entry=wrong_entry)
   
# @app.route("/calculate")
# def calculate():
#     number = request.args.get("number")
#     num_sqrt = number**0.5
#     return redirect(url_for("results",number=number,num_sqrt=num_sqrt))

# @app.route("/results")
# def results():
#     number = request.args.get("number")
#     num_sqrt=request.args.get("num_sqrt")


app.run(port=3000)