import psycopg2
from psycopg2 import sql


class Db(object):

    def __init__(self, database, user, password):
        self.__connection = psycopg2.connect(database=database, user=user, password=password, host="127.0.0.1", port="5432")
        self.__cursor = self.__connection.cursor()

    def __del__(self):
        self.close()

    def sql(self, query, *params):
        self.__cursor.execute(query, params)
        self.__connection.commit()

    def close(self):
        self.__connection.close()

    def fetch_all(self, query):
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def fetch_one(self, query, *params):
        self.__cursor.execute(query, params)
        self.__connection.commit()
        return self.__cursor.fetchone()[0]

    def clear(self, val):
        return val.replace('\'', "\\'")
