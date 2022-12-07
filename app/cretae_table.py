from abc import abstractmethod

from app.writer import IWriter


class ICreateTable():
    @abstractmethod
    def create_table(self, table_name: str) -> None:
        """Method responsible to create script table"""


class CreateTable(ICreateTable):
    def __init__(self, writer: IWriter) -> None:
        self.writer = writer
        self.table_template = (
            'CREATE TABLE IF NOT EXISTS {table_name} ('
            'id serial PRIMARY KEY NOT NULL, '
            'codigo_ibge VARCHAR (100) NOT NULL, '
            'nome_regiao VARCHAR (100) NOT NULL, '
            'tipo_regiao VARCHAR (100) NOT NULL, '
            'valor VARCHAR (100) NOT NULL, '
            'ano VARCHAR (100) NOT NULL, '
            'ano_codigo_ibge VARCHAR (100) UNIQUE NOT NULL '
            ');')
        pass

    def create_table(self, table_name: str) -> None:
        create_table = self.table_template.format(table_name=table_name)
        self.writer.write_file(table_name, create_table)
