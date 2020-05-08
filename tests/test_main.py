"""Unit tests"""

import json
import os
import time
import unittest
from collections import OrderedDict

from ib_pandas.database import Database
from ib_pandas.ib_gateway import IbGateway
from ib_pandas.main import start
from ib_pandas.utils import load_file


class TestMain(unittest.TestCase):
    """Test CSV reader"""

    @classmethod
    def setUpClass(cls):
        cls.database_name = "host.docker.internal"
        cls.database = Database(cls.database_name)
        cls.gateway = IbGateway(port=4001, host="host.docker.internal", clientId=1)
        while not cls.gateway.ping():
            print("Trying to connect to Interactive Brokers. Gateway open?")
            time.sleep(1)
        cls.ib_host = "host.docker.internal"
        cls.fixture_data = '{"foo": "bar"}'
        cwd = os.path.dirname(os.path.realpath(__file__))
        cls.universe = load_file(cwd + "/test_universe.csv")
        cls.test_universe = cwd + "/test_universe.csv"

    @classmethod
    def tearDownClass(cls):
        cls.gateway.disconnect()

    def test_main(self):
        """Test main function call"""
        result = start(self.test_universe, self.database_name)
        # expected = re.match(r"Added [0-9] rows\.", result) != None
        self.assertGreater(result, 0)

    def test_load_file(self):
        """Test loading the file"""
        result = type(self.universe)
        expected = list
        self.assertEqual(result, expected)

    def test_connect_database(self):
        """Test database connection"""
        result = self.database.ping()
        expected = True
        self.assertEqual(result, expected)

    def test_ib_gateway_connection(self):
        """Test connection to Interactive Broker gateway"""
        result = self.gateway.ping()
        expected = True
        self.assertEqual(result, expected)

    def test_fundamental_data(self):
        """Test fetching fundamental data"""
        contract = self.universe[0]
        result = type(self.gateway.fundamental_data(contract))
        expected = OrderedDict
        self.assertEqual(result, expected)

    def test_flush_database(self):
        """Test flushing data from the database"""
        result = self.database.flush()
        expected = 1
        self.assertEqual(result, expected)

    def test_import_data(self):
        """Test importing data in the database"""
        data = json.loads(self.fixture_data)
        result = self.database.import_data(keyname="mykey", data=data)
        expected = True
        self.assertEqual(result, expected)


def suite():

    """Test suite"""
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestMain("test_load_file"))
    test_suite.addTest(TestMain("test_connect_database"))
    test_suite.addTest(TestMain("test_ib_gateway_connection"))
    test_suite.addTest(TestMain("test_fundamental_data"))
    test_suite.addTest(TestMain("test_import_data"))
    test_suite.addTest(TestMain("test_flush_database"))
    test_suite.addTest(TestMain("test_main"))
    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
