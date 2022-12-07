import os
from abc import abstractmethod


class IWriter():
    @abstractmethod
    def write_file(self, table_name: str, content: str) -> None:
        """Method responsible to write on file"""


class Writer(IWriter):
    def __init__(self) -> None:
        self.file_path_template = "./artifacts/{table_name}.sql"
        pass

    def write_file(self, table_name: str, content: str) -> None:
        file_path = self.file_path_template.format(table_name=table_name)
        file = open(file_path, "a")
        file.write(content + "\n")
        file.close()

    def remove_file(self, table_name: str) -> None:
        file_path = self.file_path_template.format(table_name=table_name)
        if os.path.exists(file_path):
            os.remove(file_path)
