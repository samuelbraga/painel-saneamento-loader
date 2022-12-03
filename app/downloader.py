from abc import abstractmethod
import requests


class IDownloader():
    @abstractmethod
    def get_file(self) -> None:
        """Method responsible to get worksheet from painel do saneamento"""


class Downloader():
    def __init__(self) -> None:
        self.base_url = "https://www.painelsaneamento.org.br"
        self.path = "/explore/indicador"
        self.params = "SE%5Bg%5D=0&SE%5Bs%5D=1&SE%5Bid%5D=POP&SE%5Bo%5D=e"

    def get_file(self) -> None:
        url = f"{self.base_url}{self.path}?{self.params}"

        response = requests.get(url, stream=True)

        with open("painel_saneamento_exporter.xlsx", "wb") as handle:
            for data in response.iter_content():
                handle.write(data)
