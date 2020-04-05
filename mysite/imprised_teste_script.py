from collections import OrderedDict
from django.db.models import Count,Q
from covid19.models import *
from covid19.serializers import *

#exec(open('imprised_teste_script.py').read())
#

GRUPO_POPULACIONAL = {    
    '1':'populacao_00_04',
    '2':'populacao_05_09',
    '3':'populacao_10_14',
    '4':'populacao_15_19',
    '5':'populacao_20_24',
    '6':'populacao_25_29',
    '7':'populacao_30_39',
    '8':'populacao_40_49',
    '9':'populacao_50_59',
    '10':'populacao_60_69',
    '11':'populacao_70',
}

#Teste da view MunicipioPanoramaDataDetail
#municipio = Municipio.objects.filter(Q(uf__id=15) & Q(id=1501402)).first()
#serializer = MunicipioSerializer(municipio,many=True)
#print(serializer.data)
#print(municipio)

#Casos Suspeitos
#
# Teste da view MunicipioCasosSuspeitosLineChartDetail
#municipio = Municipio.objects.filter(Q(uf__id=15) & Q(id=1501402)).first()
#Prepara labels e data
#print("Teste da view MunicipioCasosSuspeitosLineChartDetail")
#registros_c_list = municipio.registodecasossuspeitos_set.all().values_list('created','quantidade').order_by('created')
#label = []
#data = []
#for r in registros_c_list:
#    label.append('{0:%d-%m-%Y}'.format(r[0]))
#    data.append(r[1])
#print(label)
#print(data)
#print("##########")

# Casos Confirmados
#
# Teste da view MunicipioLineChartCasosConfirmadosDetail
#municipio = Municipio.objects.filter(Q(uf__id=15) & Q(id=1501402)).first()
#Prepara as labels
#registros_c_list = municipio.registodecasoconfirmado_set.all().values_list('created').annotate(count=Count('id')).order_by('created')
#label = []
#data = []
#for r in registros_c_list:
#    label.append('{0:%d-%m-%Y}'.format(r[0]))
#    data.append(r[1])
#print(label)
#print(data)

# Teste da view MunicipioLineChartCasosConfirmadosAcumaldoDetail
#municipio = Municipio.objects.filter(Q(uf__id=15) & Q(id=1501402)).first()
#registros_c_list = municipio.registodecasoconfirmado_set.all().values_list('created').annotate(count=Count('id')).order_by('created')
#label = []
#data = []
#data_prova = []
#acumulado = 0
#for r in registros_c_list:
#    acumulado += int(r[1])
#    label.append('{0:%d-%m-%Y}'.format(r[0]))
#    data_prova.append(r[1])
#    data.append(acumulado)
#print(label)
#print(data_prova)
#print(data)
"""
# Teste da view MunicipioCasosConfirmadosGruposPopulacionalBarChartDetail
municipio = Municipio.objects.filter(Q(uf__id=15) & Q(id=1501402)).first()
label = []
data_1 = []
data_2 = [
    municipio.populacao_00_04,
    municipio.populacao_05_09,
    municipio.populacao_10_14,
    municipio.populacao_15_19,
    municipio.populacao_20_24,
    municipio.populacao_25_29,
    municipio.populacao_30_39,
    municipio.populacao_40_49,
    municipio.populacao_50_59,
    municipio.populacao_60_69,
    municipio.populacao_70,
]
for r in range(1,12):
    label.append(GRUPO_POPULACIONAL[str(r)])
    data_empty = municipio.registodecasoconfirmado_set.filter(grupo_populacional=r).count()
    data_1.append(data_empty)
print(label)
print(data_1)
print(data_2)
"""
"""
# Casos de Obitos
#

# Teste da view  MunicipioCasosObitosLineChartDetail
municipio = Municipio.objects.filter(Q(uf__id=15) & Q(id=1501402)).first()
#Prepara labels e data
print("Teste da view MunicipioCasosObitosLineChartDetail")
registros_c_list = municipio.registodecasoobito_set.all().values_list('created').annotate(count=Count('id')).order_by('created')
label = []
data = []
for r in registros_c_list:
    label.append('{0:%d-%m-%Y}'.format(r[0]))
    data.append(r[1])
print(label)
print(data)
print("##########")

# Teste da view MunicipioCasosObitosAcumaldoLineChartDetail
municipio = Municipio.objects.filter(Q(uf__id=15) & Q(id=1501402)).first()
print("Teste da view MunicipioCasosObitosAcumaldoLineChartDetail")
registros_c_list = municipio.registodecasoobito_set.all().values_list('created').annotate(count=Count('id')).order_by('created')
label = []
data = []
data_prova = []
acumulado = 0
for r in registros_c_list:
    acumulado += int(r[1])
    label.append('{0:%d-%m-%Y}'.format(r[0]))
    data_prova.append(r[1])
    data.append(acumulado)
print(label)
print(data_prova)
print(data)
print("##########")
"""

"""
# Casos de Curados
#

# Teste da view MunicipioCasosCuradosLineChartDetail
municipio = Municipio.objects.filter(Q(uf__id=15) & Q(id=1501402)).first()
#Prepara labels e data
print("Teste da view MunicipioCasosCuradosLineChartDetail")
registros_c_list = municipio.registodecasocurado_set.all().values_list('created').annotate(count=Count('id')).order_by('created')
label = []
data = []
for r in registros_c_list:
    label.append('{0:%d-%m-%Y}'.format(r[0]))
    data.append(r[1])
print(label)
print(data)
print("##########")

# Teste da view MunicipioCasosCuradosAcumaldoLineChartDetail
municipio = Municipio.objects.filter(Q(uf__id=15) & Q(id=1501402)).first()
print("Teste da view MunicipioCasosCuradosAcumaldoLineChartDetail")
registros_c_list = municipio.registodecasocurado_set.all().values_list('created').annotate(count=Count('id')).order_by('created')
label = []
data = []
data_prova = []
acumulado = 0
for r in registros_c_list:
    acumulado += int(r[1])
    label.append('{0:%d-%m-%Y}'.format(r[0]))
    data_prova.append(r[1])
    data.append(acumulado)
print(label)
print(data_prova)
print(data)
print("##########")
"""

"""
# Casos de Graves
#

# Teste da view MunicipioCasosGravesLineChartDetail
municipio = Municipio.objects.filter(Q(uf__id=15) & Q(id=1501402)).first()
#Prepara labels e data
print("Teste da view MunicipioCasosGravesLineChartDetail")
registros_c_list = municipio.registodecasograve_set.all().values_list('created').annotate(count=Count('id')).order_by('created')
label = []
data = []
for r in registros_c_list:
    label.append('{0:%d-%m-%Y}'.format(r[0]))
    data.append(r[1])
print(label)
print(data)
print("##########")

# Teste da view MunicipioCasosGravesAcumaldoLineChartDetail
municipio = Municipio.objects.filter(Q(uf__id=15) & Q(id=1501402)).first()
print("Teste da view MunicipioCasosGravesAcumaldoLineChartDetail")
registros_c_list = municipio.registodecasograve_set.all().values_list('created').annotate(count=Count('id')).order_by('created')
label = []
data = []
data_prova = []
acumulado = 0
for r in registros_c_list:
    acumulado += int(r[1])
    label.append('{0:%d-%m-%Y}'.format(r[0]))
    data_prova.append(r[1])
    data.append(acumulado)
print(label)
print(data_prova)
print(data)
print("##########")
"""
"""
# Variação de casos confirmados por dia
uf = UF.objects.get(id=15)
labels = []
data = []
data_temp_dict = {}
data_temp = []
for m in uf.municipio_set.all():
    registros = m.registodecasoconfirmado_set.all().values_list('created').annotate(count=Count('id')).order_by('created')
    for r in registros:
             data_temp.append(r)
print(data_temp)
data_temp.sort(key=lambda tup: tup[0])
print(data_temp)
for d in data_temp:
     if '{0:%d-%m-%Y}'.format(d[0]) in data_temp_dict:
             data_temp_dict['{0:%d-%m-%Y}'.format(d[0])] += d[1]
     else:
             data_temp_dict['{0:%d-%m-%Y}'.format(d[0])] = d[1]
print(data_temp_dict)
for key in data_temp_dict:
    labels.append(key)
    data.append(data_temp_dict[key])
print(labels)
print(data)
"""

"""
# evolução de casos confirmados, acumulado dia a dia
uf = UF.objects.get(id=15)
labels = []
data = []
data_temp_dict = {}
data_temp = []
for m in uf.municipio_set.all():
    registros = m.registodecasoconfirmado_set.all().values_list('created').annotate(count=Count('id')).order_by('created')
    for r in registros:
             data_temp.append(r)
print(data_temp)
data_temp.sort(key=lambda tup: tup[0])
print(data_temp)
for d in data_temp:
     if '{0:%d-%m-%Y}'.format(d[0]) in data_temp_dict:
             data_temp_dict['{0:%d-%m-%Y}'.format(d[0])] += d[1]
     else:
             data_temp_dict['{0:%d-%m-%Y}'.format(d[0])] = d[1]
print(data_temp_dict)
total = 0
for key in data_temp_dict:
    labels.append(key)
    total += data_temp_dict[key]
    data.append(total)
print(labels)
print(data)
"""

"""
# Evolução de casos confirmados por cidade
uf = UF.objects.get(id=15)
data_temp = {}
for m in uf.municipio_set.all():
    totoal_registros = m.registodecasoconfirmado_set.all().count()
    if totoal_registros:
        data_temp[m.nome] = totoal_registros
print(data_temp)
labels = []
data = []
acumulado = 0
for key in sorted(data_temp, key=data_temp.get, reverse=True):
    labels.append(key)
    data.append(data_temp[key])
print(labels)
print(data)
"""
"""
# Casos Confirmados pro grupo etário:
uf = UF.objects.get(id=15)
labels =[    
    'População de 00a04',
    'População de 05a09',
    'População de 10a14',
    'População de 15a19',
    'População de 20a24',
    'População de 25a29',
    'População de 30a39',
    'População de 40a49',
    'População de 50a59',
    'População de 60a69',
    'População de 70+',
]
data = [0,0,0,0,0,0,0,0,0,0,0]
for m in uf.municipio_set.all():
    data[0] = data[0] + m.populacao_00_04_infectada
    data[1] = data[1] + m.populacao_05_09_infectada
    data[2] = data[2] + m.populacao_10_14_infectada 
    data[3] = data[3] + m.populacao_15_19_infectada 
    data[4] = data[4] + m.populacao_20_24_infectada 
    data[5] = data[5] + m.populacao_25_29_infectada 
    data[6] = data[6] + m.populacao_30_39_infectada 
    data[7] = data[7] + m.populacao_40_49_infectada 
    data[8] = data[8] + m.populacao_50_59_infectada 
    data[9] = data[9] + m.populacao_60_69_infectada
    data[10] = data[10] + m.populacao_70_infectada
print(labels)
print(data)
"""
"""
# Casos Confirmados agrupados por sexo
uf = UF.objects.get(id=15)
labels = ['masculino','feiminino','desconhecido']
data = [0,0,0]
for m in uf.municipio_set.all():
    data[0] += m.registodecasoconfirmado_set.filter(sexo=0).count()
    data[1] += m.registodecasoconfirmado_set.filter(sexo=1).count()
    data[2] += m.registodecasoconfirmado_set.filter(sexo=2).count()
print(labels)
print(data)
"""