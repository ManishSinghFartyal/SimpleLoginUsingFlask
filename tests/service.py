import tests.User as user

def check_login(username,password):
	if username in user.user_details:
		if password == user.user_details[username]['Password']:
			return True
		else:
			return False
	else:
		return False

def register_user(userid,username,password,address,contact):
	new_user = {
	userid:
		{
		"Name":username,
		"Password":password,
		"Contact":contact,
		"Address":address
		}
	}
	print(new_user)
	user.user_details.update(new_user)
	print(user.user_details)