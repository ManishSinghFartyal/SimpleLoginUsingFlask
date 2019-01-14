import tests.User as user
import pymongo
import tests.db as db
def get_user(user_id):
	table=db.get_db()
	doc=table.find_one({'_id':user_id})
	print(doc)
	return doc
	
get_user("Saurabh123")