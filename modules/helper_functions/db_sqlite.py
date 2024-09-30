import sqlite3
import os.path


class DBConnection:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, "users.db")
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.c = self.conn.cursor()

    def create_table(self, table, fields):
        with self.conn:
            fields = ", ".join([f for f in fields])
            self.c.execute("""CREATE TABLE IF NOT EXISTS{} ({})""".format(table, fields))
            return {"status_code": 200}

    def retrieve_table(self, table):
        with self.conn:
            self.c.execute("SELECT * FROM {}".format(table))
        return self.c.fetchall()

    # excepts table name and a the new record in the form of dictionary
    def insert_row(self, table, new_rec):
        values = ",".join(["?" for _ in new_rec.keys()])
        raw = (*new_rec.values(),)
        with self.conn:
            self.c.execute("INSERT INTO {} VALUES ({}) ".format(table,values), raw)
        return {"status_code": 200}

    # updating field
    def update_row(self, table, field, old_val, new_val):
        var = "`{0}` = '{1}'".format(field, new_val)
        where = "`{0}` = '{1}'".format(field, old_val)
        with self.conn:
            self.c.execute("""UPDATE {0} SET {1} 
                        WHERE {2}""".format(table, var, where))
        return {"status_code": 200}

    # remove row by criteria
    def remove_row(self, table, field, val):
        where = "`{0}` = '{1}'".format(field, val)
        with self.conn:
            self.c.execute("DELETE from {0} WHERE {1}".format(table, where))
        return {"status_code": 200}


db = DBConnection()



