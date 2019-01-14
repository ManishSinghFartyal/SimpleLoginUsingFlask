import pymongo
def get_db():
	myclient=pymongo.MongoClient("mongodb://localhost:27017")
	mydb=myclient['GitHub']
	mycol=mydb['user_details']
	return mycol