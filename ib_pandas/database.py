"""Database manager"""
from rejson import Client, Path


class Database:
    """Database handler"""

    def __init__(self, database_name, port=6379):
        self.database = Client(host=database_name, port=port, decode_responses=True)

    def flush(self):
        """Flushing a certain table of the database"""
        return self.database.flushdb()

    def import_data(self, keyname, data):
        """Load data into the database"""
        return self.database.jsonset(keyname, Path.rootPath(), data)

    def ping(self):
        """Tests the connection"""
        return self.database.ping()
