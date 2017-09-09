# Links e Comandos do Tutorial "Capturando Dados Sem Dor de Cabeça"

## Material

- [Slides palestra "Gênero e Número: Python ajudando a entender as questões de gênero brasileiras"](http://bit.ly/pysul-gn)
- [Gênero e Número](http://generonumero.media/)
- [Vídeo da palestra "rows: Liberando Dados Com Um Comando"](https://www.youtube.com/watch?v=XzvDsZf_Spwi&list=PL461EA301371D1BD6&index=19)
- [Vídeo da palestra "Dados Tabulares: Qual o Pior Formato?"](https://www.youtube.com/watch?v=mVkWZVtZDT0)
- [Documentação rows](http://turicas.info/rows)
- [Canal Pythonic Café no YouTube](https://www.youtube.com/c/PythonicCafe)


## Fontes de dados

- [IBGE Nomes](http://www.ibge.gov.br/censo2010/apps/nomes/)
- [Sports Reference Brazil Summer 2012](sports-reference.com/olympics/countries/BRA/summer/2012/)


## Bibliotecas e Ferramentas

- [pyenv](https://github.com/pyenv/pyenv)
- [Biblioteca JSONBender](https://github.com/Onyo/jsonbender)
- [Biblioteca rows](https://github.com/turicas/rows)
- [Biblioteca splinter](https://splinter.readthedocs.io/en/latest/)
- [Biblioteca tapioca-wrapper](https://github.com/vintasoftware/tapioca-wrapper)
- [rows: exemplos como biblioteca](https://github.com/turicas/rows/tree/develop/examples/library)
- [rows: exemplos da command-line interface](https://github.com/turicas/rows/tree/develop/examples/cli)
- [rows: exemplo `rows query` com SQL join](https://github.com/turicas/rows/blob/develop/examples/cli/query.sh)
- [webscrapper](http://webscraper.io/)
- [Chrome Developer Tools](https://developer.chrome.com/devtools)


## Código

- [Repositório de código GN classificação de logradouros por gênero](https://github.com/generonumero/logradouros/)
- [Repositório de código GN extração dados históricos olimpíadas](https://github.com/generonumero/olimpiadas/)
- [Repositório de código GN análise de dados da educação superior](https://github.com/generonumero/educacao/)


## Comandos

Criar virtualenv:

```bash
python3 -m venv tutorial-pysul
```

Ativar virtualenv:

```bash
source tutorial-pysul/bin/activate
```

Instalar dependências:

```bash
pip install -r requirements.txt
```

Rodar script de forma interativa:

```bash
ipython -i nomes.py
```

Baixar e extrair tabela em HTML e exibir no terminal como texto:

```bash
URL=https://www.sports-reference.com/olympics/countries/BRA/summer/2012/
rows print $URL
```

Baixar, extrair e converter uma tabela em HTML para CSV:

```bash
URL=https://www.sports-reference.com/olympics/countries/BRA/summer/2012/
rows convert $URL olimpiadas.csv
```

Baixar e extrair uma tabela em HTML, rodar uma consulta SQL nos dados e exibir o resultado no terminal como texto:

```bash
QUERY='SELECT athlete, gender, gold FROM table1 WHERE gold > 0'
URL=https://www.sports-reference.com/olympics/countries/BRA/summer/2012/
rows query $QUERY $URL
```

Baixar e extrair uma tabela em HTML, rodar uma consulta SQL nos dados e extrair o resultado para um arquivo XLS:

```bash
QUERY='SELECT athlete, gender, gold FROM table1 WHERE gold > 0'
URL=https://www.sports-reference.com/olympics/countries/BRA/summer/2012/
rows query "$SQL" $URL --output=gold.xls
```
