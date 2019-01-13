import tests.User as user
def get_user(user_id):
	online_user = user.user_details[user_id]
	return online_user

print(get_user("Manish123"))