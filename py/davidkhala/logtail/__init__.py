# https://betterstack.com/docs/logs/python/#logging-from-python
import logging

from logtail import LogtailHandler


class Ingestion:

    def __init__(self, token: str, host: str):
        """
        :param token:
        :param host: Ingestion host is scoped to each BetterStack Source. With or without host are both accepted
        """
        assert host.endswith('.betterstackdata.com')
        self.handler = LogtailHandler(
            source_token=token,
            host=host,
            raise_exceptions=True
        )

    def attach(self, logger: logging.Logger):
        logger.addHandler(self.handler)

    def detach(self, logger: logging.Logger):
        logger.removeHandler(self.handler)
