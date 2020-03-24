import requests
import json
from covid19.models import UF,Municipio
from datetime import datetime

"""
#Para executar esses script entre no shell do Django e execute o 
# seguinte comando exec(open('util_script_import_ibge_ufs_municipios.py').read())
#Depois que fiz este script descobrir que existe  uma pacote em python que falicita isso
# https://github.com/leogregianin/ibge
"""

#Constantes
#IBGE urls
IBGE_UFS_URL = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'
#Para pegar o ID dos estados acessa IBGE_UFS_URL pelo navegador que mostra o JSON, nele tem os ID's.
UF_ID='15'
IBGE_UF_URL = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{UF}'.format(UF=UF_ID)
IGBE_UF_MUNICIPIOS_URL = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{UF}/municipios'

def get_json_data_from_url(url):
    headers = {'Content-Type': 'application/json'}
    response = requests.get(
        url=url,
        headers=headers,
    )
    response.raise_for_status()
    return response.json()

# Variaveis temporarias e auxiliares da função
# import_ufs_ibge
ufs_list = []
ufs_data = get_json_data_from_url(IBGE_UFS_URL)
# import_uf_ibge
uf_data = get_json_data_from_url(IBGE_UF_URL)
uf_instance = ''

# Função para persistir os dados das UFS vindos
# da API do IBGE via json
def import_ufs_ibge(ufs_data):
    for uf_data in ufs_data:
        print('Importandndo dados da UF{UF}'.format(UF=uf_data.get('nome')))
        uf = UF(
            id = uf_data.get('id'),
            nome = uf_data.get('nome'),
            sigla = uf_data.get('sigla')
        )
        ufs_list.append(uf)
        uf.save()
        #print(uf)

#Importa apenas uma UF
def import_uf_ibge(uf_data):
        print('Importandndo dados da UF {UF}'.format(UF=uf_data.get('nome')))
        uf_instance = UF(
            id = uf_data.get('id'),
            nome = uf_data.get('nome'),
            sigla = uf_data.get('sigla')
        )
        uf_instance.save()
        #print(uf)
        return uf_instance

def import_uf_municipios_ibge(uf):
    ibge_uf_municipios = IGBE_UF_MUNICIPIOS_URL.format(UF=uf.id)
    uf_municipios_data = get_json_data_from_url(ibge_uf_municipios)
    print('Importandndo dados dos municipios da UF {UF}'.format(UF=uf.nome))
    for uf_municipio_data in uf_municipios_data:
        municipio = Municipio(
            uf = uf,
            id = uf_municipio_data.get('id'),
            nome = uf_municipio_data.get('nome'),
        )
        municipio.save()
        #print(municipio)
    

#Executar
#Importa dados da UF's e gera uma lista de objetos
# UF que será utilzada na importação dos Municipios.
#import_ufs_ibge(ufs_data)
#Importa os municpios de cada estado.
#for uf in ufs_list:
#    import_uf_municipios_ibge(uf)

#Se preferir importar dados de apenas uma UF
uf_instance = import_uf_ibge(uf_data)
import_uf_municipios_ibge(uf_instance)