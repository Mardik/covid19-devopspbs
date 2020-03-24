import requests
import json
from covid19.models import UF,Municipio
from datetime import datetime

"""
#Para executar esses script entre no shell do Django e execute o 
# seguinte comando exec(open('util_script_import_brasilio_covid19.py').read())
# 
"""

BRASIL_IO_COVID19_UFS_MUNICPIOS_DATA = 'https://brasil.io/api/dataset/covid19/caso/data?format=json'


def get_json_data_from_url(url):
    headers = {'Content-Type': 'application/json'}
    response = requests.get(
        url=url,
        headers=headers,
    )
    response.raise_for_status()
    return response.json()

casos_por_localidades = get_json_data_from_url(BRASIL_IO_COVID19_UFS_MUNICPIOS_DATA)['results']

for casos_por_localidade in casos_por_localidades:
    print(casos_por_localidade)