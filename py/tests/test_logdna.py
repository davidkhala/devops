import logging
import os
import unittest

from davidkhala.mezmo import Ingestion


class LogIngestionTestCase(unittest.TestCase):
    def test_send(self):
        api_key = os.environ['LOGDNA_INGESTION_KEY']
        i = Ingestion(api_key)
        self.assertTrue(i.connect())
        log = logging.getLogger(__name__)
        log.setLevel(logging.DEBUG)
        i.attach(log)
        log.debug("hello world")


if __name__ == '__main__':
    unittest.main()
