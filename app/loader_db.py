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
        self.insert_template = (
            'INSERT INTO public.{table_name} '
            '(codigo_ibge, nome_regiao, '
            'tipo_regiao, valor, ano, ano_codigo_ibge) '
            'VALUES '
            '({codigo_ibge}, \'{nome_regiao}\', '
            '\'{tipo_regiao}\', {valor}, {ano}, \'{ano_codigo_ibge}\') '
            'ON CONFLICT (ano_codigo_ibge) DO NOTHING;')

    def load_pandas_to_postgres_sql(
        self,
        df: pandas.DataFrame,
        table_name: str
    ) -> None:
        print(table_name, "STARTED")
        columns = df.columns
        anos = [2021, 2020, 2019, 2018, 2017, 2016,
                2015, 2014, 2013, 2012, 2011, 2010]
        for _, row in df.iterrows():
            nome_regiao: str = row['Nome_Regiao']
            codigo_ibge = int(row['Codigo_IBGE'])
            tipo_regiao: str = row['Tipo_Regiao']
            for ano in range(1, 12):
                if (row[str(columns[ano])] != '-'):
                    valor = float(row[str(columns[ano])])
                    insert = self.insert_template.format(
                        table_name=table_name,
                        codigo_ibge=codigo_ibge,
                        nome_regiao=nome_regiao,
                        tipo_regiao=tipo_regiao,
                        valor=valor,
                        ano=anos[ano],
                        ano_codigo_ibge=f'{anos[ano]}-{codigo_ibge}')
                    self.writer.write_file(table_name, insert)
        print(table_name, "DONE")
