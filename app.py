from flask import Flask,render_template,request,url_for,redirect
from tests import service

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("home.html")


@app.route("/about")
def about():
	return render_template("About.html")



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
			return render_template("home.html")	
		else:
			return redirect(url_for("about"))
	else:
		return redirect(url_for('about'))

@app.route("/login")
def login():
	return render_template("login.html")

if __name__=='__main__':
	app.run()