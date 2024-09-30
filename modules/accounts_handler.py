from modules.helper_functions.db_sqlite import db


class AccountsHandler:
    """A helper class for API accounts for basic auth
    (ideally we would save it in separate DB in this case I'll put this in the same DB)"""

    def create_users_table(self):
        db.create_table("accounts", ["username text", "password text"])

    def get_accounts(self):
        res = {}
        _lst = db.retrieve_table("accounts")
        for record in _lst:
            res.update({record[0]: record[1]})
        return res


accounts = AccountsHandler()

