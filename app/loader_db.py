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
        for _, row in df.iterrows():
            nome_regiao: str = row['Nome_Regiao']
            codigo_ibge = int(row['Codigo_IBGE'])
            tipo_regiao: str = row['Tipo_Regiao']
            for ano in range(2010, 2021):
                if (row[f'{ano}.0'] != '-'):
                    valor = float(row[f'{ano}.0'])
                    insert = self.insert_template.format(
                        table_name=table_name,
                        codigo_ibge=codigo_ibge,
                        nome_regiao=nome_regiao,
                        tipo_regiao=tipo_regiao,
                        valor=valor,
                        ano=ano,
                        ano_codigo_ibge=f'{ano}-{codigo_ibge}')
                    self.writer.write_file(table_name, insert)
