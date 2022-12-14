# PAINEL SANEAMENTO LOADER

Painel sanemamento loader é um projeto que visa extrair, modelar, transformar, gerar arquivos de inserção em um banco de dados e persistência dos indicadores presentes no painel do sanemanto em um banco de dados relacional

O mecanismo irá gerar diversos arquivos de inserção para banco de dados postgres na pasta `artifacts`. Esses arquivos de inserção serão executados em uma banco de dados.

Para referênciar o banco de dados desejado substitua os valores contido no arquivo `.env.template` e o renomeie para `.env`.

## Docker

Você pode utilizar o mecanismo via [docker](hhttps://www.docker.com/). Para isso, você pode seguir o tutorial de instalção no [link](https://docs.docker.com/engine/install/)

É necessário a utilização de uma extensão do docker que é o [docker-compose](https://docs.docker.com/compose/). Você pode fazer a instalação dessa extensão pelo [link](https://docs.docker.com/compose/install/)

Após ter a ferramenta na sua máquina basta executar o seguinte comanda:

```bash
make run
```

## Development

O mecanismo foi desenvolvido utilizando [python](https://www.python.org/) na versão 3.10.8. Você pode instlar essa versão especifica pelo [link](https://www.python.org/downloads/release/python-3109/)

Ou utilizar o [pyenv](https://github.com/pyenv/pyenv) que é uma ferramenta que auxilia no gerenciamento de versões do python

Será necessário realizar a instalação do [pipenv](https://pipenv.pypa.io/en/latest/). Qee é uma biblioteca responsável por fazer o gerenciamento das dependências do mecanismo 

```bash
pip install pipenv
```

Em seguinda, realizar a criação do virtual envrionment juntamente com o download das dependências do projeto

```bash
pipenv install --system --skip-lock
```

É impotante, seguir os padrões de estilo e codificações do projeto. Para se certificar que está tudo certo. Você pode executar o seguinte comando

```bash
make verify
```

## Adição de novos indicadores

Adicione os metadados do indicador no arquivo `indicators.json` seguindo o padrão existente.
## License

[MIT](https://choosealicense.com/licenses/mit/)