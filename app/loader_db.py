from abc import abstractmethod

import pandas
from app.writer import IWriter


class ILoaderDB():
    @abstractmethod
    def load_pandas_to_postgres_sql(
        self,
        df: pandas.DataFrame,
        table_name: str
    ) -> None:
        """Method responsible to load panda dataframe to sql file"""


class LoaderDB(ILoaderDB):
    def __init__(self, writer: IWriter) -> None:
        self.writer = writer
        self.insert_value_template = (
            '({codigo_ibge}, \'{nome_regiao}\', '
            '\'{tipo_regiao}\', {valor}, {ano}, \'{ano_codigo_ibge}\'),')
        self.insert_template = (
            'INSERT INTO public.{table_name} '
            '(codigo_ibge, nome_regiao, '
            'tipo_regiao, valor, ano, ano_codigo_ibge) '
            'VALUES')

    def load_pandas_to_postgres_sql(
        self,
        df: pandas.DataFrame,
        table_name: str
    ) -> None:
        print(table_name, "STARTED")
        insert = self.insert_template.format(table_name=table_name)
        self.writer.write_file(table_name, insert)
        columns = df.columns
        for _, row in df.iterrows():
            nome_regiao: str = row['Nome_Regiao']
            codigo_ibge = int(row['Codigo_IBGE'])
            tipo_regiao: str = row['Tipo_Regiao']
            for ano in range(1, 12):
                if (row[str(columns[ano])] != '-'):
                    valor = float(row[str(columns[ano])])
                    insert_value = self.insert_value_template.format(
                        codigo_ibge=codigo_ibge,
                        nome_regiao=nome_regiao,
                        tipo_regiao=tipo_regiao,
                        valor=valor,
                        ano=ano,
                        ano_codigo_ibge=f'{ano}-{codigo_ibge}')
                    self.writer.write_file(table_name, insert_value)
        self.writer.remove_last_character(table_name)
        self.writer.write_file(table_name, ';')
        print(table_name, "DONE")
