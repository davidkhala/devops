import logging
import os
import unittest

from davidkhala.logtail import Ingestion

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class LogIngestionTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        token = os.environ.get('LOGTAIL_TOKEN')
        host = os.environ.get('LOGTAIL_HOST') or 's1241007.eu-nbg-2.betterstackdata.com'
        cls.i = Ingestion(token, host)
        cls.i.attach(logger)

    def test_send(self):
        logger.info('no https')

    @classmethod
    def tearDownClass(cls):
        cls.i.detach(logger)


if __name__ == '__main__':
    unittest.main()
