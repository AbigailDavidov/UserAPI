from modules.helper_functions.db_sqlite import db


class UserAction:
    """A helper class to preform some user related CRUD operations"""

    def create_users_table(self):
        db.create_table("users", ["email text", "password text"])

    def get_users(self):
        res = []
        users_lst = db.retrieve_table("users")
        for record in users_lst:
            rec = {}
            rec["email"] = record[0]
            rec["password"] = record[1]
            res.append(rec)
        return res

    def add_user(self, user):
        dct = {'email':user.email, 'password': user.password}
        users_lst = db.retrieve_table("users")
        # search for duplicates
        for record in users_lst:
            if record[0] == user.email:
                return "user exists", 409
        return db.insert_row("users",dct)

    def update_user(self, user, new_val):
        users = self.get_users()
        # find user
        for u in users:
            if u["email"] == user.email and u["password"] == user.password:
                return db.update_row("users", "password", u["password"], new_val)
        return "couldn't find user", 404

    def delete_user(self, user):
        users = self.get_users()
        # find user
        for u in users:
            if u["email"] == user.email and u["password"] == user.password:
                return db.remove_row("users", "email", user.email)
        return "couldn't find user", 404


user_action = UserAction()

