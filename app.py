from flask import Flask,request,render_template, redirect, flash, session
import mlab
from models.register import Register
from models.register import Sound
app = Flask(__name__)
app.config["SECRET_KEY"] = "<d9H\9nhpv4eRD@$mT*bg(Z@=bSCF:*=Q-anNQv3*4a;~[qUCeNx+"
mlab.connect()

@app.route('/', methods=["GET","POST"])
def home():
    if request.method == "GET":
        sounds = []
        users_login = []
        data = Sound.objects()
        users = Register.objects()
        for sound in data:
            item = {
                "name": sound.name,
                "link": sound.link,
                "classIcon": sound.classIcon,
                "playing": False,
                "pause" : True,
                "audio": None,
                "loading": True,
            }
            sounds.append(item)
        for user in users:
            db_user = {
                "username": user.username,
                "password": user.password
            }
            users_login.append(db_user)
        return render_template("homepage-out.html", dataHtml=sounds, users=users_login)

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = Register.objects(username=username).first()
        if user != None:
            if user.password==password :
                session["token"] = username
                session["logged"] = True
                return redirect("/")
            else:
                return redirect("/")
        else:
            return redirect("/")

@app.route("/logout")
def logout():
    if "token" in session:
        del session["token"]
        session["logged"] = False
        return redirect("/")
    else:
        return redirect("/")

@app.route('/signup',methods=["GET","POST"])
def signup():
    if request.method == "POST":
        username= request.form["username"]
        password=request.form["password"]
        dateOfBirth = request.form["dateOfBirth"]
        email = request.form["email"]
        f_objects =  Register(username=username, password= password,dateOfBirth=dateOfBirth,email=email)
        f_objects.save()
        return redirect("/")
        
if __name__ == '__main__':
  app.run(debug=True)