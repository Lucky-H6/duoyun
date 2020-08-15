class User:
    def __init__(self, username, password, user_type):
        self.username = username
        self.password = password
        self.user_type = user_type

    def store_user(self):
        # !TODO
        # store user info into database
        pass

    @classmethod
    def check_user(cls, username, password):
        # !TODO
        # check if a username and password is stored in database
        # return user:0  publisher:1  error:-1
        pass

    @classmethod
    def check_username(cls, username):
        # !TODO
        # check if the username is in database
        # return 0 for not, 1 for in.
        pass

