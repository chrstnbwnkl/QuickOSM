"""Manage downloader."""

import logging

from qgis.core import Qgis, QgsFileDownloader
from qgis.PyQt.QtCore import QByteArray, QEventLoop, QUrl, QUrlQuery

__copyright__ = 'Copyright 2021, 3Liz'
__license__ = 'GPL version 3'
__email__ = 'info@3liz.org'

LOGGER = logging.getLogger('QuickOSM')


class Downloader:
    """Manage downloader."""

    def __init__(self, url: str = None):
        """Constructor."""
        if url is None:
            url = 'https://nominatim.openstreetmap.org/search?'

        self._url = QUrl(url)
        self.result_path = None
        self.errors = []

    def error(self, messages: str):
        """Store the messages error"""
        self.errors = messages

    @staticmethod
    def canceled():
        """Display the status in logger"""
        LOGGER.info('Request canceled')
        # TODO, need to handle this to stop the process.

    @staticmethod
    def completed():
        """Display the status in logger"""
        LOGGER.info('Request completed')

    def download(self):
        """Download the data"""
        # We use POST instead of GET
        # We move the "data" GET parameter into the POST request
        url_query = QUrlQuery(self._url)
        data = "data={}".format(url_query.queryItemValue('data'))
        url_query.removeQueryItem('data')
        self._url.setQuery(url_query)
        downloader = QgsFileDownloader(
            self._url,
            self.result_path,
            delayStart=True,
            httpMethod=Qgis.HttpMethod.Post,
            data=QByteArray(str.encode(data))
        )
        loop = QEventLoop()
        downloader.downloadExited.connect(loop.quit)
        downloader.downloadError.connect(self.error)
        downloader.downloadCanceled.connect(self.canceled)
        downloader.downloadCompleted.connect(self.completed)
        downloader.startDownload()
        loop.exec_()
