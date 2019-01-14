import User as user
import service as service
import db as db

#print(user.user_details)
#print(service.check_login("Akib15","12345"))
#service.register_user("Manish125","Manish Singh","12345","Kothrud","8865048253")
table = db.get_db()
doc= table.find();
for x in doc:
	print(x)