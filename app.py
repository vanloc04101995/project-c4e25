from flask import Flask,request,render_template, redirect, flash, sessio
import mlap
from modles.register import Register
app = Flask(__name__)
app.config["SECRET_KEY"] = "<d9H\9nhpv4eRD@$mT*bg(Z@=bSCF:*=Q-anNQv3*4a;~[qUCeNx+"
mlap.connect()
@app.route('/')
def home():
    return render_template("home.html")

@route('/login', methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = Register.objects(username=username).first()
        if user!=None:
            if user.password==password :
                session["token"] = username
                return redirect("/menu" +str(user.id))
            else:
                flash("Invalid password")
                return render_template("login.html")
        else:
            flash("Not found")
            return render_template("login.html")

@app.route("/logout")
def logout():
    if "token" in session:
        del session["token"]
        return redirect("/")
    else:
        return redirect("/")

@app.route('/signUp',methods=["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("signUp.html")
    elif request.method == "POST":
        username= request.form["username"]
        password=request.form["password"]
        dateOfBirth = request.form["dateOfBirth"]
        emailOrSdt = request.form["emailOrSdt"]
        f_objects =  Register(username=username, password= password,dateOfBirth=dateOfBirth,emailOrSdt=emailOrSdt)
        f_objects.save()
        return redirect("/menu"+str(f_objects.id))

if __name__ == '__main__':
  app.run(debug=True)