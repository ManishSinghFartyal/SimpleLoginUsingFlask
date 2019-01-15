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
	if 'userid' in session:
		return redirect(url_for('profile'))
	else:
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
	if 'userid' in session:
		userid = session['userid']
		online_user=uservice.get_user(userid)
		return render_template("profile.html",user=online_user,userid=userid)
	else:
		return render_template("login.html")

@app.route("/quote")
def quote():
	if 'userid' in session:		
		return render_template("quotes.html")
	else:
		return render_template("login.html")

@app.route("/logout")
def logout():
	session.clear()
	return redirect(url_for('index'))

@app.route("/newquote",methods=['GET','POST'])
def newquote():
	if 'userid' in session:
		if request.method =='POST':
			title = request.form['title']
			quote = request.form['quote']
			uservice.insert_quote(title,quote,session['userid'])
			return redirect(url_for('profile'))
		else:
			return redirect(url_for('index'))
	else:
		return redirect(url_for('index'))

@app.route("/read_quote/<article_id>")
def read_quote(article_id):
	article = uservice.get_article(article_id,session['userid'])
	return render_template("ReadArticle.html",article=article)

if __name__=='__main__':
	app.run()