import io

import requests
import requests_cache
import rows


requests_cache.install_cache('olimpiadas')
url = 'https://www.sports-reference.com/olympics/countries/BRA/summer/2012/'
response = requests.get(url)
table = rows.import_from_html(io.BytesIO(response.content))
rows.export_to_csv(table, 'olimpiadas.csv')
