class User:
    """A very basic user class just to showcase some functionality"""

    def __init__(self, email, password):
        self.email = email
        self.password = password
        # I assumed input integrity due to lack of time and no explicit requirement.

    def __repr__(self):
         return "user('{}', '{}')".format(self.email, self.password)

