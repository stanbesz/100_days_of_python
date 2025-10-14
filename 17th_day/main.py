class User:
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print("New user created...")

    def follow(self,user):
        user.followers += 1
        self.following += 1


user_1 = User("001","Stan") #always calls init

print(user_1.username)

user_2 = User("002","Not_Stan")

print(user_2.id)

user_1.follow(user_2)
print(f"User 1 followers: {user_1.followers}")
print(f"User 2 followers: {user_2.followers}")
