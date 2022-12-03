from abc import abstractmethod
from app.downloader import Downloader, IDownloader


class ILoader():
    @abstractmethod
    def loader_painel_saneamento() -> None:
        """Method responsible to loader painel do saneamento on database"""


class Loader(ILoader):
    def __init__(self) -> None:
        pass

    def loader_painel_saneamento(self) -> None:
        downloader: IDownloader = Downloader()
        downloader.get_file()
