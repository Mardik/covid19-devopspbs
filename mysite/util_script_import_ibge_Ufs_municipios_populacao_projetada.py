import locale
import csv
from covid19.models import UF,Municipio
from datetime import datetime
from django.db.models import Q

#exec(open('util_script_import_ibge_Ufs_municipios_populacao_projetada.py').read())

BASE_PATH = 'dados-externos/Populacao_projetada_2019.csv'

def import_ibge_uf_municipios_dado_populacao_projetada(base_path):
    print("Importando dados sobre população projetada dos Municipios para ano de 2019")
    with open(base_path,'r') as f:
        reader = csv.DictReader(f,delimiter=';')
        for dict_r in reader:
            municipio = Municipio.objects.get(id=dict_r['cod'])
            municipio.populacao_projetada = dict_r['popula']
            print(municipio.populacao_projetada)
            municipio.save()

import_ibge_uf_municipios_dado_populacao_projetada(BASE_PATH)