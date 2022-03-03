import os

import psycopg2


DB_USERNAME = os.environ.get("database-user", "postgres")
DB_PASSWORD = os.environ.get("database-password", "postgres")
DB_NAME = os.environ.get("database-name", "postgres")
DB_HOST = os.environ.get("database-host", "postgresql.ifrn-demo.svc.cluster.local")
DB_PORT = os.environ.get("database-port", "5432")


class FakeCursor:
    def __init__(self, details):
        self.details = details

    def close(self):
        pass

    def execute(self, *args):
        pass

    def fetchone(self):
        return self.details.args


class Database:
    def __init__(self):
        self._conn = None
        self._cursor = None

    def __enter__(self):
        try:
            self._conn = psycopg2.connect(user=DB_USERNAME,
                                          password=DB_PASSWORD,
                                          host=DB_HOST,
                                          port=DB_PORT,
                                          database=DB_NAME)

            return self._conn.cursor()
        except psycopg2.OperationalError as details:
            return FakeCursor(details)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._cursor is not None:
            self._cursor.close()
            self._cursor = None

        if self._conn is not None:
            self._conn.close()
            self._conn = None


with Database() as db:
    db.execute("SELECT version();")
    record = db.fetchone()
    print(record)
