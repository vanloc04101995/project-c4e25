from flask import Flask,request,render_template, redirect, flash, session
import mlap
from modles.register import Register
app = Flask(__name__)
app.config["SECRET_KEY"] = "<d9H\9nhpv4eRD@$mT*bg(Z@=bSCF:*=Q-anNQv3*4a;~[qUCeNx+"
mlap.connect()
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login', methods=["GET","POST"])
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
                return redirect("/register" +str(user.id))
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
def signUp():
    if request.method == "GET":
        return render_template("signUp.html")
    elif request.method == "POST":
        username= request.form["username"]
        password=request.form["password"]
        dateOfBirth = request.form["dateOfBirth"]
        emailOrSdt = request.form["emailOrSdt"]
        print(type(emailOrSdt))
        f_objects =  Register(username=username, password= password,dateOfBirth=dateOfBirth,emailOrSdt=emailOrSdt)
        f_objects.save()
        return redirect("/register"+str(f_objects.id))
@app.route('/register')
def register():
    return render_template("register.html")
if __name__ == '__main__':
  app.run(debug=True)