class User:
    def __init__(self, id,username ):
        self.id = id
        self.username = username
        self.follower = 0
        self.following = 0
    def follow(self, user):
        user.follower += 1
        self.following += 1

user_1 = User("01", "Roney Chowdhury")
user_2 = User("02", "Mahamudul Chowdhury")

print("before following")
print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)

user_1.follow(user_2)
print("After following")
print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)