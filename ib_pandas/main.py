"""Read a CSV file"""

import getopt
import sys

from ib_pandas.database import Database
from ib_pandas.ib_gateway import IbGateway
from ib_pandas.utils import load_file


def start(filename, database):
    """Main function handling the program steps"""
    universe = load_file(filename)  # Load csv file with stocks
    database = Database(database)  # Connect to Redis
    gateway = IbGateway(port=4001, host="host.docker.internal")  # Connect to IB
    database.flush()  # Flush the database
    rows_count = 0
    for stock in universe:
        data = gateway.fundamental_data(stock)  # Load fundamental data
        if database.import_data(keyname=stock["symbol"], data=data):  # Add rows
            rows_count = rows_count + 1
    print("Added " + str(rows_count) + " rows.")
    return rows_count


def usage():
    """Example usage"""
    print("ib_pandas.py -f <path_to_universe> -d <database_address>")


def main():
    """Main function parsing arguments"""
    try:
        # pylint: disable=unused-variable
        opts, args = getopt.getopt(sys.argv[1:], "f:d:h", ["filename=", "database="])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)
    filename = "universe.csv"
    database = "http://server.local"
    for opt, arg in opts:
        if opt == "-h":
            usage()
            sys.exit()
        elif opt in ("-f", "--filename"):
            filename = arg
        elif opt in ("-d", "--database"):
            database = arg
        else:
            assert False, "unhandled option"
    start(filename, database)


if __name__ == "__main__":
    main()
