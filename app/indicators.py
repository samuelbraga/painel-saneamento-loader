import json
from abc import abstractmethod
from typing import Any


class IIndicators():
    @abstractmethod
    def get_indicators_metadata(self) -> Any:
        """Method responsible to search and get indicators metadata"""


class Indicators():
    def __init__(self) -> None:
        pass

    def get_indicators_metadata(self) -> Any:
        with open("indicators.json") as file:
            data = json.load(file)
        return data
