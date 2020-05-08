"""Interactive Brokers Gateway manager"""

import time
from collections import namedtuple

import xmltodict
from ib_insync import IB, Contract


class IbGateway:
    """Interactive Brokers functions to fetch data"""

    def __init__(self, host, port, clientId=0):
        self.ib_gateway = IB()
        self.ib_gateway.connect(host, port, clientId=clientId)

    def fundamental_data(self, contract):
        """Load fundamental data from Interactive Brokers"""
        ib_contract = Contract(**contract)
        fundamental_data = self.ib_gateway.reqFundamentalData(
            ib_contract, reportType="ReportsFinStatements"
        )
        return xmltodict.parse(fundamental_data)

    def flush(self, tablename):
        """Remove all data from the table"""

    def ipmort_data(self, tablename, data):
        """Write data into the table"""

    def ping(self):
        """Pings Interactive Brokers gateway"""
        return self.ib_gateway.isConnected()

    def disconnect(self):
        """Disconnect from Interactive Brokers"""
        self.ib_gateway.disconnect()
