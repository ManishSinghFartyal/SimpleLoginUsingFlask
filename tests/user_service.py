import tests.User as user
import pymongo
import tests.db as db

table1=db.get_db()
def get_user(user_id):
	table=db.get_db()
	doc=table.find_one({'_id':user_id})	
	return doc

def insert_quote(title,quote,user_id):
	doc=table1.find_one({'_id':user_id})
	print(doc)
	if doc.get('Articles',None) is None:
		print(doc)
		table1.update_one({'_id':user_id},{'$push':{'Articles':{'article_id':1,'title':title,'quote':quote}}})
	else:
		length =len(doc["Articles"])
		length +=1
		table1.update_one({'_id':user_id},{'$push':{'Articles':{'article_id':length,'title':title,'quote':quote}}})

def get_article(article_id,user_id):
	id_article=int(article_id)
	doc=table1.find_one({'_id':user_id})	
	articles =doc['Articles']
	for article in articles:
		print(article['article_id']," ",article_id)
		if article['article_id'] == id_article:
			print(article)
			return article
	return None