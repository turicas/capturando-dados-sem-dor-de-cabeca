import requests
import requests_cache
import rows


def convert_api_data(female, male):
    if not female and not male:
        return None
    female = female[0] if female else {}
    male = male[0] if male else {}

    alternatives = []
    if female and female['nomes']:
        alternatives += female['nomes'].split(',')
    if male and male['nomes']:
        alternatives += male['nomes'].split(',')

    return {
            'name': female['nome'] if female else male['nome'],
            'freq_f': female.get('freq'),
            'freq_m': male.get('freq'),
            'alternatives': ','.join(sorted(set(alternatives))),
            }

def name_ibge(name):
    url = 'http://servicodados.ibge.gov.br/api/v1/censos/nomes/basica'

    query_string = {'nome': name, 'sexo': 'f'}
    response_female = requests.get(url, params=query_string)
    query_string = {'nome': name, 'sexo': 'm'}
    response_male = requests.get(url, params=query_string)

    return convert_api_data(response_female.json(), response_male.json())

def convert_names(names, csv_output):
    table = rows.import_from_dicts([name_ibge(name)
                                    for name in names
                                    if name_ibge(name)])
    rows.export_to_csv(table, csv_output)

requests_cache.install_cache('nomes-ibge')
convert_names(['renata', 'claudia', 'iara', 'marcelo', 'felipe', 'jose',
               'juciano', 'matheus', 'rodrigo', 'gabriel', 'rafael'],
              'names.csv')
