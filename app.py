from flask import Flask,render_template,request,url_for,redirect,session
from tests import service
from tests import user_service as uservice

app = Flask(__name__)
app.secret_key = 'Manish'
@app.route("/")
def index():
	return render_template("home.html")


@app.route("/about")
def about():
	return render_template("About.html")


@app.route("/profile")
def profile():
	if 'userid' in session:
		userid = session['userid']
		online_user=uservice.get_user(userid)
		return render_template("profile.html",user=online_user,userid=userid)
	else:
		return redirect(url_for('login'))


@app.route("/register")
def register():
	return render_template("register.html")


@app.route("/register_user",methods=['GET','POST'])
def register_user():	
	if request.method == 'POST':
		username = request.form['un']
		fullname=request.form['fn']
		password = request.form['pwd']
		contact = request.form['contact']
		address = request.form['add']
		print(username)
		service.register_user(username,fullname,password,address,contact)
		return render_template("home.html")	
	else:
		return redirect(url_for('about'))

@app.route("/login_user",methods=['GET','POST'])
def login_user():
	
	if request.method == 'POST':
		username = request.form['un']
		password = request.form['pwd']
		result= service.check_login(username,password)
		print(result)
		if result == True:
			session['userid']=username
			return redirect(url_for("profile"))	
		else:
			return redirect(url_for("about"))
	else:
		return redirect(url_for('about'))

@app.route("/login")
def login():
	return render_template("login.html")

if __name__=='__main__':
	app.run()