import pypyodbc

class DB(object):
    _db_connection = None
    _db_cur = None

    def __init__(self, instance):
        self._connection_string = 'DSN=%s' % (instance)
        self._db_connection = pypyodbc.connect(self._connection_string)
        #self._db_connection.current_schema = 'marval'
        self._db_cur = self._db_connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        if exception_type is not None:
            raise
        self._db_connection.close()

    def query(self, query, params=None):
        if params is None:
            return self._db_cur.execute(query)
        return self._db_cur.execute(query, params)

    def fetchall(self, query, params=None):
        return self.query(query, params).fetchall()

    def close(self):
        self._db_connection.close()

def main():
    pass

if __name__ == '__main__':
    main()
