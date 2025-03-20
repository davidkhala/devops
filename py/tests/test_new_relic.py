import unittest

from davidkhala.newrelic.log import Ingestion


class LogIngestionTestCase(unittest.TestCase):

    def test_send(self):
        i = Ingestion()
        i.send("log")


if __name__ == '__main__':
    unittest.main()
