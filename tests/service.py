import tests.User as user
import tests.db as db
import pymongo

def check_login(username,password):
	print(username,"  ",password)
	table =db.get_db()
	doc = table.find_one({"_id":username,"Password":password})
	if doc is None:
		return False
	else:
		return True

def register_user(userid,username,password,address,contact):
	new_user ={
		"_id":userid,
		"Name":username,
		"Password":password,
		"Contact":contact,
		"Address":address
		}
	print(new_user)
	table=db.get_db()	
	x=table.insert_one(new_user)
	print(x.inserted_id)
