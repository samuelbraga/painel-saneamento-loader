from abc import abstractmethod

import pandas
from app.cretae_table import CreateTable, ICreateTable
from app.downloader import Downloader, IDownloader
from app.indicators import IIndicators, Indicators
from app.loader_db import ILoaderDB, LoaderDB
from app.reader import IReader, Reader
from app.writer import IWriter, Writer


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
        writer: IWriter = Writer()
        reader: IReader = Reader()

        create_table: ICreateTable = CreateTable(writer)
        loader_db: ILoaderDB = LoaderDB(writer)

        indicators_metadata = indicators.get_indicators_metadata()
        for indicator_metadata in indicators_metadata['indicators']:
            indicator_key = indicator_metadata['indicator']
            indicator_params = indicator_metadata['params']
            writer.remove_file(indicator_key)
            create_table.create_table(indicator_key)
            downloader.get_file(indicator_params)
            df: pandas.DataFrame = reader.reder_file()
            loader_db.load_pandas_to_postgres_sql(df, indicator_key)
