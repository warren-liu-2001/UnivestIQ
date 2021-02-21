connectionstring = "postgres://uofthax8hack@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&sslrootcert=<src/cc-ca.crt&options=--cluster=mature-otter-855"

username = "uofthax8hack"

host = "free-tier.gcp-us-central1.cockroachlabs.cloud"

port = 26257

database_co = "mature-otter-855.defaultdb"

password = "UofTHacks2021"

import psycopg2
from account import Account

conn = psycopg2.connect(
    database=database_co,
    user='username',
    password=password,
    sslmode='disable',
    sslrootcert='UnivestIQ/backend/src/cc-ca.crt',
    port=26257,
    host='free-tier.gcp-us-central1.cockroachlabs.cloud',
    options="--cluster=mature-otter-855"
)

class DBConn:

    def __init__(self):
        self.conn = conn

    def save_user_data(self, userid, uname, password, email):

        with self.conn.cursor() as cur:
            cur.execute("UPDATE users SET name = name - %s WHERE id = %s",
                        (uname, userid))
        self.conn.commit()

        with self.conn.cursor() as cur:
            cur.execute("UPDATE users SET password = password - %s WHERE id = %s",
                        (password, userid))
        self.conn.commit()

        with self.conn.cursor() as cur:
            cur.execute("UPDATE users SET email = email- %s WHERE id = %s",
                        (email, userid))
        self.conn.commit()

    def export_user_data(self) -> List[Account]:
        with conn.cursor() as cur:
            DATA = []
            cur.execute("SELECT * FROM userinfo")
            rows = cur.fetchall()
            for row in rows:
                DATA.append(row)

            listacc = []
            for DATUM in DATA:
                acc = Account(DATUM[0], DATUM[2], DATUM[3], DATUM[1])
                listacc.append(acc)
            return listacc


















