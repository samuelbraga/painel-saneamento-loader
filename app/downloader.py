from abc import abstractmethod

import requests
from dynaconf import settings


class IDownloader():
    @abstractmethod
    def get_file(self, params: str) -> None:
        """Method responsible to get worksheet from painel do saneamento"""


class Downloader():
    def __init__(self) -> None:
        self.base_url = settings('base_url')
        self.path = settings('path')

    def get_file(self, params) -> None:
        url = f"{self.base_url}{self.path}?{params}"

        response = requests.get(url, stream=True)
        output = open('painel_saneamento_exporter.xlsx', 'wb')
        output.write(response.content)
        output.close()
