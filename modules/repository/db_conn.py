import os

import psycopg2
import psycopg2.extras
from modules.utils.config import POSTGRES_HOST, POSTGRES_USER, \
    POSTGRES_PORT, POSTGRES_PASSWORD, POSTGRES_DATABASE


class Connection:

    def __init__(self):
        self.host = POSTGRES_HOST
        self.user = POSTGRES_USER
        self.password = POSTGRES_PASSWORD
        self.database = POSTGRES_DATABASE
        self.port = POSTGRES_PORT

    def open_connection(self):
        return psycopg2.connect(host=self.host,
                                user=self.user,
                                password=self.password,
                                database=self.database)

    def get_postgres_uri(self):
        host = self.host
        port = self.port  # 5432
        password = self.password
        user, db_name = self.user, self.database
        return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
