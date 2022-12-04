from abc import abstractmethod

import pandas
from app.downloader import Downloader, IDownloader
from app.indicators import IIndicators, Indicators
from app.reader import IReader, Reader


class ILoader():
    @abstractmethod
    def loader_painel_saneamento() -> None:
        """Method responsible to loader painel do saneamento on database"""


class Loader(ILoader):
    def __init__(self) -> None:
        pass

    def loader_painel_saneamento(self) -> None:
        indicators: IIndicators = Indicators()
        downloader: IDownloader = Downloader()
        reader: IReader = Reader()

        indicators_metadata = indicators.get_indicators_metadata()
        for indicator_metadata in indicators_metadata['indicators']:
            # indicator_key = indicator_metadata['indicator']
            indicator_params = indicator_metadata['params']
            downloader.get_file(indicator_params)
            df: pandas.DataFrame = reader.reder_file()
            print(df.head(2))
