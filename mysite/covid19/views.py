from random import randint
from django.db.models import Count,Q
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from  .serializers import *
# Create your views here.

#utils
def dynamicColor():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return "rgb({},{},{},1)".format(str(r),str(g),str(b))

SEXO = {
    '0': 'masculino',
    '1': 'feminino',
    '2': 'desconhecido',
}

"""
class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'covid19/charts.html')

class IndexPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'covid19/index.html')
"""

# Views que retorna os CasosSuspeitos por data, evolução pontual
class MunicipioCasosSuspeitosLineChartDetail(APIView):
    def get(self,request, pk):
        municipio = Municipio.objects.filter(Q(id=pk)).first()
        registros_c_list = municipio.registodecasossuspeitos_set.all().values_list('created','quantidade').order_by('created')
        labels = []
        data = []
        for r in registros_c_list:
            labels.append('{0:%d-%m-%Y}'.format(r[0]))
            data.append(r[1])

        if data:
            data = {
                "datacollection": {
                "labels": labels,
                "datasets": [
                    {
                        "label": 'Casos Confirmados',
                        "backgroundColor": dynamicColor(),
                        "pointBackgroundColor": 'white',
                        "borderWidth": 1,
                        "pointBorderColor": '#249EBF',
                        "data": data,
                    }
                ]
                }
            }
        else:
            data = None
        return Response(data)

# Views que retorna os casos confirmados por data, evolução pontual
class MunicipioCasosConfirmadosLineChartDetail(APIView):
    def get(self,request, pk):
        municipio = Municipio.objects.filter(Q(id=pk)).first()
        registros_c_list = municipio.registodecasoconfirmado_set.all().values_list('created').annotate(count=Count('id')).order_by('created')
        labels = []
        data = []
        for r in registros_c_list:
            labels.append('{0:%d-%m-%Y}'.format(r[0]))
            data.append(r[1])

        if data:
            data = {
                "datacollection": {
                "labels": labels,
                "datasets": [
                    {
                        "label": 'Casos Confirmados',
                        "backgroundColor": dynamicColor(),
                        "pointBackgroundColor": 'white',
                        "borderWidth": 1,
                        "pointBorderColor": '#249EBF',
                        "data": data,
                    }
                ]
                }
            }
        else:
            data = None
        return Response(data)

# Views que retorna os casos confirmados por data, evolução acumulada
class MunicipioCasosConfirmadosAcumaldoLineChartDetail(APIView):
    def get(self,request, pk):
        municipio = Municipio.objects.filter(Q(id=pk)).first()
        registros_c_list = municipio.registodecasoconfirmado_set.all().values_list('created').annotate(count=Count('id')).order_by('created')
        labels = []
        data = []
        #data_prova = []
        acumulado = 0
        for r in registros_c_list:
            acumulado += int(r[1])
            labels.append('{0:%d-%m-%Y}'.format(r[0]))
            #data_prova.append(r[1])
            data.append(acumulado)

        if data:
            data = {
                "datacollection": {
                "labels": labels,
                "datasets": [
                    {
                        "label": 'Casos Confirmados',
                        "backgroundColor": dynamicColor(),
                        "pointBackgroundColor": 'white',
                        "borderWidth": 1,
                        "pointBorderColor": '#249EBF',
                        "data": data,
                    }
                ]
                }
            }
        else:
            data = None
        return Response(data)

class MunicipioCasosConfirmadosSegregadosPeloSexoPieChartDetail(APIView):
    def get(self,request, pk):
        municipio = Municipio.objects.filter(Q(id=pk)).first()
        labels = []
        data = []
        backgroundColor = []

        for r in range(0,3):
            labels.append(SEXO[str(r)])
            data_empty = municipio.registodecasoconfirmado_set.filter(sexo=r).count()
            data.append(data_empty)
            backgroundColor.append(dynamicColor())

        if data:
            data = {
                "datacollection": {
                "labels": labels,
                "datasets": [
                    {
                        "label": 'Casos Confirmados',
                        "backgroundColor": backgroundColor,
                        "pointBackgroundColor": 'white',
                        "borderWidth": 1,
                        "pointBorderColor": '#249EBF',
                        "data": data,
                    }
                ]
                }
            }
        else:
            data = None
        return Response(data)    

class MunicipioCasosConfirmadosSegregadosPorIdadeXPopulacaoHBarChartDetail(APIView):
    def get(self,request, pk):
        municipio = Municipio.objects.filter(Q(id=pk)).first()
        labels = []
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
            labels.append(municipio.GRUPO_POPULACIONAL[str(r)])
            data_empty = municipio.registodecasoconfirmado_set.filter(grupo_populacional=r).count()
            data_1.append(data_empty)

        if data_1 and data_2:
            data = {
                "datacollection": {
                "labels": labels,
                "datasets": [
                    {
                        "label": 'População por Grupo Etario',
                        "backgroundColor": dynamicColor(),
                        "pointBackgroundColor": 'white',
                        "borderWidth": 1,
                        "pointBorderColor": '#249EBF',
                        "data": data_1,
                    },
                    {
                        "label": 'População por Grupo Etario Infectada',
                        "backgroundColor": '#000000',
                        "pointBackgroundColor": 'white',
                        "borderWidth": 1,
                        "pointBorderColor": '#249EBF',
                        "data": data_2,
                    }
                ]
                }
            }
        else:
            data = None
        return Response(data)

class MunicipioCasosConfirmadosPorGrupoPopulacionalBarChartDetail(APIView):
    def get(self,request, pk):
        municipio = Municipio.objects.filter(Q(id=pk)).first()
        labels = []
        data = []

        for r in range(1,12):
            labels.append(municipio.GRUPO_POPULACIONAL[str(r)])
            data_empty = municipio.registodecasoconfirmado_set.filter(grupo_populacional=r).count()
            data.append(data_empty)

        if data:
            data = {
                "datacollection": {
                "labels": labels,
                "datasets": [
                    {
                        "label": 'Casos Confirmados',
                        "backgroundColor": dynamicColor(),
                        "pointBackgroundColor": 'white',
                        "borderWidth": 1,
                        "pointBorderColor": '#249EBF',
                        "data": data,
                    }
                ]
                }
            }
        else:
            data = None
        return Response(data)   

# Views que retorna os Casos de Obitos por data, evolução pontual
class MunicipioCasosObitosLineChartDetail(APIView):
    def get(self,request, pk):
        municipio = Municipio.objects.filter(Q(id=pk)).first()
        registros_c_list = municipio.registodecasoobito_set.all().values_list('created').annotate(count=Count('id')).order_by('created')
        labels = []
        data = []
        for r in registros_c_list:
            labels.append('{0:%d-%m-%Y}'.format(r[0]))
            data.append(r[1])

        data = {
            "datacollection": {
            "labels": labels,
            "datasets": [
                {
                    "label": 'Casos Confirmados',
                    "backgroundColor": dynamicColor(),
                    "pointBackgroundColor": 'white',
                    "borderWidth": 1,
                    "pointBorderColor": '#249EBF',
                    "data": data,
                }
            ]
            }
        }
        return Response(data)

# Views que retorna os Casos de Obitos por data, evolução acumulada
class MunicipioCasosObitosAcumaldoLineChartDetail(APIView):
    def get(self,request, pk):
        municipio = Municipio.objects.filter(Q(id=pk)).first()
        registros_c_list = municipio.registodecasoobito_set.all().values_list('created').annotate(count=Count('id')).order_by('created')
        labels = []
        data = []
        #data_prova = []
        acumulado = 0
        for r in registros_c_list:
            acumulado += int(r[1])
            labels.append('{0:%d-%m-%Y}'.format(r[0]))
            #data_prova.append(r[1])
            data.append(acumulado)

        data = {
            "datacollection": {
            "labels": labels,
            "datasets": [
                {
                    "label": 'Casos Confirmados',
                    "backgroundColor": dynamicColor(),
                    "pointBackgroundColor": 'white',
                    "borderWidth": 1,
                    "pointBorderColor": '#249EBF',
                    "data": data,
                }
            ]
            }
        }
        return Response(data)

# Views que retorna os Casos de Curados por data, evolução pontual
class MunicipioCasosCuradosLineChartDetail(APIView):
    def get(self,request, pk):
        municipio = Municipio.objects.filter(Q(id=pk)).first()
        registros_c_list = municipio.registodecasocurado_set.all().values_list('created').annotate(count=Count('id')).order_by('created')
        labels = []
        data = []
        for r in registros_c_list:
            labels.append('{0:%d-%m-%Y}'.format(r[0]))
            data.append(r[1])

        data = {
            "datacollection": {
            "labels": labels,
            "datasets": [
                {
                    "label": 'Casos Confirmados',
                    "backgroundColor": dynamicColor(),
                    "pointBackgroundColor": 'white',
                    "borderWidth": 1,
                    "pointBorderColor": '#249EBF',
                    "data": data,
                }
            ]
            }
        }
        return Response(data)

# Views que retorna os Casos de Curados por data, evolução acumulada
class MunicipioCasosCuradosAcumaldoLineChartDetail(APIView):
    def get(self,request, pk):
        municipio = Municipio.objects.filter(Q(id=pk)).first()
        registros_c_list = municipio.registodecasocurado_set.all().values_list('created').annotate(count=Count('id')).order_by('created')
        labels = []
        data = []
        #data_prova = []
        acumulado = 0
        for r in registros_c_list:
            acumulado += int(r[1])
            labels.append('{0:%d-%m-%Y}'.format(r[0]))
            #data_prova.append(r[1])
            data.append(acumulado)

        data = {
            "datacollection": {
            "labels": labels,
            "datasets": [
                {
                    "label": 'Casos Confirmados',
                    "backgroundColor": dynamicColor(),
                    "pointBackgroundColor": 'white',
                    "borderWidth": 1,
                    "pointBorderColor": '#249EBF',
                    "data": data,
                }
            ]
            }
        }
        return Response(data)

# Views que retorna os Casos de Graves por data, evolução pontual
class MunicipioCasosGravesLineChartDetail(APIView):
    def get(self,request, pk):
        municipio = Municipio.objects.filter(Q(id=pk)).first()
        registros_c_list = municipio.registodecasograve_set.all().values_list('created').annotate(count=Count('id')).order_by('created')
        labels = []
        data = []
        for r in registros_c_list:
            labels.append('{0:%d-%m-%Y}'.format(r[0]))
            data.append(r[1])

        data = {
            "datacollection": {
            "labels": labels,
            "datasets": [
                {
                    "label": 'Casos Confirmados',
                    "backgroundColor": dynamicColor(),
                    "pointBackgroundColor": 'white',
                    "borderWidth": 1,
                    "pointBorderColor": '#249EBF',
                    "data": data,
                }
            ]
            }
        }
        return Response(data)

# Views que retorna os Casos Graves por data, evolução acumulada
class MunicipioCasosGravesAcumaldoLineChartDetail(APIView):
    def get(self,request, pk):
        municipio = Municipio.objects.filter(Q(id=pk)).first()
        registros_c_list = municipio.registodecasograve_set.all().values_list('created').annotate(count=Count('id')).order_by('created')
        labels = []
        data = []
        #data_prova = []
        acumulado = 0
        for r in registros_c_list:
            acumulado += int(r[1])
            labels.append('{0:%d-%m-%Y}'.format(r[0]))
            #data_prova.append(r[1])
            data.append(acumulado)

        data = {
            "datacollection": {
            "labels": labels,
            "datasets": [
                {
                    "label": 'Casos Confirmados',
                    "backgroundColor": dynamicColor(),
                    "pointBackgroundColor": 'white',
                    "borderWidth": 1,
                    "pointBorderColor": '#249EBF',
                    "data": data,
                }
            ]
            }
        }
        return Response(data)

class MunicipioRegistrosDeCasosGravesList(APIView):
    def get(self,request, m_pk):
        registos = RegistoDeCasoGrave.objects.filter(Q(municipio=m_pk))
        data = RegistoDeCasoGraveSerializer(registos,many=True).data
        return Response(data)

class MunicipioRegistrosDeCasosCuradosList(APIView):
    def get(self,request, m_pk):
        registos = RegistoDeCasoCurado.objects.filter(Q(municipio=m_pk))
        data = RegistoDeCasoCuradoSerializer(registos,many=True).data
        return Response(data)

class MunicipioRegistrosDeCasosObitosList(APIView):
    def get(self,request, m_pk):
        registos = RegistoDeCasoObito.objects.filter(Q(municipio=m_pk))
        data = RegistoDeCasoObitoSerializer(registos,many=True).data
        return Response(data)

class MunicipioRegistrosDeCasosConfirmadosList(APIView):
    def get(self,request, m_pk):
        registos = RegistoDeCasoConfirmado.objects.filter(Q(municipio=m_pk))
        data = RegistoDeCasoConfirmadoSerializer(registos,many=True).data
        return Response(data)

class MunicipioRegistrosDeCasosSuspeitosList(APIView):
    def get(self,request, m_pk):
        registos = RegistoDeCasosSuspeitos.objects.filter(Q(municipio=m_pk))
        data = RegistoDeCasosSuspeitosSerializer(registos,many=True).data
        return Response(data)

class MunicipioPanoramaDataDetail(APIView):
    def get(self,request,pk):
        municipio = Municipio.objects.filter(Q(id=pk))
        data = MunicipioSerializer(municipio,many=True).data
        return Response(data)

class MunicipiosList(APIView):
    def get(self,request):
        municipios = Municipio.objects.all()
        data = MunicipioSerializer(municipios,many=True).data
        return Response(data)

class UFCasosConfirmadosPorCidadeBarChartDetail(APIView):
    def get(self,request,pk):
        uf = UF.objects.get(id=pk)
        data_temp = {}
        for m in uf.municipio_set.all():
            totoal_registros = m.registodecasoconfirmado_set.all().count()
            if totoal_registros:
                data_temp[m.nome] = totoal_registros

        labels = []
        data = []
        acumulado = 0
        for key in sorted(data_temp, key=data_temp.get, reverse=True):
            labels.append(key)
            data.append(data_temp[key])

        if data:
            data = {
                "datacollection": {
                    "labels": labels,
                    "datasets": [
                        {
                            "label": 'Casos Confirmados',
                            "backgroundColor": dynamicColor(),
                            "pointBackgroundColor": 'white',
                            "borderWidth": 1,
                            "pointBorderColor": '#249EBF',
                            "data": data,
                        }
                    ]
                }
            }
        else:
            data = None

        return Response(data)

#Casos Confirmados pro grupo etário:
class UFCasosConfirmadosPorGrupoEtarioBarChartDetail(APIView):
    def get(self,request,pk):
        uf = UF.objects.get(id=pk)
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

        if data:
            data = {
                "datacollection": {
                "labels": labels,
                "datasets": [
                    {
                        "label": 'Casos Confirmados',
                        "backgroundColor": dynamicColor(),
                        "pointBackgroundColor": 'white',
                        "borderWidth": 1,
                        "pointBorderColor": '#249EBF',
                        "data": data,
                    }
                ]
                }
            }
        else:
            data = None
        return Response(data)

#Casos Confirmados agrupados por sexo
class UFCasosConfirmadosSegregadosPorSexoPieChartDetail(APIView):
    def get(self,request,pk):
        uf = UF.objects.get(id=pk)
        labels = ['masculino','feiminino','desconhecido']
        data = [0,0,0]
        backgroundColor = [dynamicColor(),dynamicColor(),dynamicColor()]
        for m in uf.municipio_set.all():
            data[0] += m.registodecasoconfirmado_set.filter(sexo=0).count()
            data[1] += m.registodecasoconfirmado_set.filter(sexo=1).count()
            data[2] += m.registodecasoconfirmado_set.filter(sexo=2).count()
        if data:
            data = {
                "datacollection": {
                "labels": labels,
                "datasets": [
                    {
                        "label": 'Casos Confirmados',
                        "backgroundColor": backgroundColor,
                        "pointBackgroundColor": 'white',
                        "borderWidth": 1,
                        "pointBorderColor": '#249EBF',
                        "data": data,
                    }
                ]
                }
            }
        else:
            data = None
        return Response(data)

class UFCasosConfirmadosAcumaldoLineChartDetail(APIView):
    def get(self,request,pk):
        uf = UF.objects.get(id=pk)
        labels = []
        data = []
        data_temp_dict = {}
        data_temp = []
        for m in uf.municipio_set.all():
            registros = m.registodecasoconfirmado_set.all().values_list('created').annotate(count=Count('id')).order_by('created')
            for r in registros:
                    data_temp.append(r)

        data_temp.sort(key=lambda tup: tup[0])

        for d in data_temp:
            if '{0:%d-%m-%Y}'.format(d[0]) in data_temp_dict:
                    data_temp_dict['{0:%d-%m-%Y}'.format(d[0])] += d[1]
            else:
                    data_temp_dict['{0:%d-%m-%Y}'.format(d[0])] = d[1]

        total = 0
        for key in data_temp_dict:
            labels.append(key)
            total += data_temp_dict[key]
            data.append(total)

        if data:
            data = {
                "datacollection": {
                "labels": labels,
                "datasets": [
                    {
                        "label": 'Casos Confirmados',
                        "backgroundColor": dynamicColor(),
                        "pointBackgroundColor": 'white',
                        "borderWidth": 1,
                        "pointBorderColor": '#249EBF',
                        "data": data,
                    }
                ]
                }
            }
        else:
            data = None
        return Response(data)

class UFCasosConfirmadosLineChartDetail(APIView):
    def get(self,request,pk):
        uf = UF.objects.get(id=pk)
        labels = []
        data = []
        data_temp_dict = {}
        data_temp = []
        for m in uf.municipio_set.all():
            registros = m.registodecasoconfirmado_set.all().values_list('created').annotate(count=Count('id')).order_by('created')
            for r in registros:
                    data_temp.append(r)

        data_temp.sort(key=lambda tup: tup[0])

        for d in data_temp:
            if '{0:%d-%m-%Y}'.format(d[0]) in data_temp_dict:
                    data_temp_dict['{0:%d-%m-%Y}'.format(d[0])] += d[1]
            else:
                    data_temp_dict['{0:%d-%m-%Y}'.format(d[0])] = d[1]

        for key in data_temp_dict:
            labels.append(key)
            data.append(data_temp_dict[key])

        if data:
            data = {
                "datacollection": {
                "labels": labels,
                "datasets": [
                    {
                        "label": 'Casos Confirmados',
                        "backgroundColor": dynamicColor(),
                        "pointBackgroundColor": 'white',
                        "borderWidth": 1,
                        "pointBorderColor": '#249EBF',
                        "data": data,
                    }
                ]
                }
            }
        else:
            data = None
        return Response(data)

class UFPanoramaDataDetail(APIView):
    def get(self,request,pk):
        uf = UF.objects.filter(Q(id=pk))
        data = UFSerializer(uf,many=True).data
        return Response(data)

class UFList(APIView):
    def get(self,request):
        ufs = UF.objects.all()
        data = UFSerializer(ufs,many=True).data
        return Response(data)

class IBGEGruposPopulacionais(APIView):
    def get(self,request):
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
        return Response(GRUPO_POPULACIONAL)

class UFPanoramaDatasList(APIView):
    pass

class UFPanoramaChartCasosSuspeitosList(APIView):
    pass

class UFPanoramaChartCasosConfirmadosList(APIView):
    pass
