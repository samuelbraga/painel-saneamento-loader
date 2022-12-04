from abc import abstractmethod
from typing import List, Tuple

import pandas


class IReader():
    @abstractmethod
    def reder_file() -> pandas.DataFrame:
        """Method responsible to reder workseeht"""


class Reader():
    def __init__(self) -> None:
        pass

    def _calc_region_and_ibge_code(
        self,
        localidades: List[Tuple[str, str, int]]
    ) -> Tuple[List[str], List[int]]:
        codigo_ibge: List[int] = []
        tipo_regiao: List[str] = []
        for item in localidades:
            if (item[0] == 'Brasil'):
                codigo_ibge.append(item[1])
                tipo_regiao.append('Pais')
            else:
                tipo_regiao.append(item[1])
                codigo_ibge.append(item[2])
        return (tipo_regiao, codigo_ibge)

    def _clean_local_column(self, df: pandas.DataFrame) -> pandas.DataFrame:
        df['Localidade'] = df['Localidade'].str.replace("(", "", regex=True)
        df['Localidade'] = df['Localidade'].str.replace(")", "", regex=True)
        df['Localidade'] = df['Localidade'].str.split()

        localidades = df['Localidade'].to_list()
        tipo_regiao, codigo_ibge = self._calc_region_and_ibge_code(localidades)

        df = df.assign(Codigo_IBGE=codigo_ibge)
        df = df.assign(Tipo_Regiao=tipo_regiao)
        df['Localidade'] = df['Localidade'].str[0]
        return df

    def reder_file(self) -> pandas.DataFrame:
        df = pandas.read_excel(
            io='painel_saneamento_exporter.xlsx',
            engine='openpyxl')

        df = df.iloc[1:, :]
        df.reset_index(drop=True, inplace=True)
        df.columns = df.iloc[0]
        df = df[1:]
        df.reset_index(drop=True, inplace=True)

        df = self._clean_local_column(df)
        return df
