import locale
import csv
from covid19.models import UF,Municipio
from datetime import datetime
from django.db.models import Q

BASE_PATH = 'dados-externos/CENSO-2010/{UF_ID}-Censo.csv'
UFS_IDS = UF.objects.all().order_by('id').values_list('id', flat=True)

#Para executar esses script entre no shell do Django e execute o 
# seguinte comando exec(open('util_script_import_igbe_uf_censo.py').read())

#Função que vai extrair dados populacionais dos municipios das UF's
# para alimentar o modelo Municipios.
# filds alimentados:
#


#Sabemos que essa função precisa ser otimizada, e tem um possivel erro,
# que é qnd uma UF tem dois municipios com o mesmo nome, mais 
# fique a vontade!
def import_ibge_uf_municipios_dados_populacionais(base_path,UF_ID):
    print("Importando dados da UF {UF} do Censo de 2010".format(UF=UF_ID))
    with open(base_path,'r') as f:
        reader = csv.DictReader(f,delimiter=',')
        for dict_r in reader:
            if dict_r['Posição'] == '3.3.1.1':
                municipio = Municipio.objects.filter(Q(uf__id=UF_ID) & Q(nome=dict_r['Localidade'])).first()
                municipio.populacao_00_04 = dict_r['2010']
                #print(municipio.populacao_00_04)
                municipio.save()
            if dict_r['Posição'] == '3.3.1.2':
                municipio = Municipio.objects.filter(Q(uf__id=UF_ID) & Q(nome=dict_r['Localidade'])).first()
                municipio.populacao_05_09 = dict_r['2010']
                #print(municipio.populacao_00_04)
                municipio.save()
            if dict_r['Posição'] == '3.3.1.3':
                municipio = Municipio.objects.filter(Q(uf__id=UF_ID) & Q(nome=dict_r['Localidade'])).first()
                municipio.populacao_10_14 = dict_r['2010']
                #print(municipio.populacao_00_04)
                municipio.save()
            if dict_r['Posição'] == '3.3.1.4':
                municipio = Municipio.objects.filter(Q(uf__id=UF_ID) & Q(nome=dict_r['Localidade'])).first()
                municipio.populacao_15_19 = dict_r['2010']
                #print(municipio.populacao_00_04)
                municipio.save()
            if dict_r['Posição'] == '3.3.1.5':
                municipio = Municipio.objects.filter(Q(uf__id=UF_ID) & Q(nome=dict_r['Localidade'])).first()
                municipio.populacao_20_24 = dict_r['2010']
                #print(municipio.populacao_00_04)
                municipio.save()
            if dict_r['Posição'] == '3.3.1.6':
                municipio = Municipio.objects.filter(Q(uf__id=UF_ID) & Q(nome=dict_r['Localidade'])).first()
                municipio.populacao_25_29 = dict_r['2010']
                #print(municipio.populacao_00_04)
                municipio.save()
            if dict_r['Posição'] == '3.3.1.7':
                municipio = Municipio.objects.filter(Q(uf__id=UF_ID) & Q(nome=dict_r['Localidade'])).first()
                municipio.populacao_30_39 = dict_r['2010']
                #print(municipio.populacao_00_04)
                municipio.save()
            if dict_r['Posição'] == '3.3.1.8':
                municipio = Municipio.objects.filter(Q(uf__id=UF_ID) & Q(nome=dict_r['Localidade'])).first()
                municipio.populacao_40_49 = dict_r['2010']
                #print(municipio.populacao_00_04)
                municipio.save()
            if dict_r['Posição'] == '3.3.1.9':
                municipio = Municipio.objects.filter(Q(uf__id=UF_ID) & Q(nome=dict_r['Localidade'])).first()
                municipio.populacao_50_59 = dict_r['2010']
                #print(municipio.populacao_00_04)
                municipio.save()
            if dict_r['Posição'] == '3.3.1.10':
                municipio = Municipio.objects.filter(Q(uf__id=UF_ID) & Q(nome=dict_r['Localidade'])).first()
                municipio.populacao_60_69 = dict_r['2010']
                #print(municipio.populacao_00_04)
                municipio.save()
            if dict_r['Posição'] == '3.3.1.11':
                municipio = Municipio.objects.filter(Q(uf__id=UF_ID) & Q(nome=dict_r['Localidade'])).first()
                municipio.populacao_70 = dict_r['2010']
                #print(municipio.populacao_00_04)
                municipio.save()
             
#Executa
#Importa os dados
#Intera sobre todos as UF's
#for UF_ID in UFS_IDS:
#    base_path = BASE_PATH.format(UF_ID=UF_ID)
#    import_ibge_uf_municipios_dados_populacionais(base_path,UF_ID)

#Intera sobre uma UF especifica
UF_ID = 15
base_path = BASE_PATH.format(UF_ID=UF_ID)
import_ibge_uf_municipios_dados_populacionais(base_path,UF_ID)