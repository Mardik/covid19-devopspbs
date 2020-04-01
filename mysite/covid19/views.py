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

"""
class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'covid19/charts.html')

class IndexPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'covid19/index.html')
"""

class MunicipiosList(APIView):
    def get(self,request):
        municipios = Municipio.objects.all()
        data = MunicipioSerializer(municipios,many=True).data
        return Response(data)


class MunicipioPanoramaDataDetail(APIView):
    def get(self,request, uf_pk, pk):
        municipio = Municipio.objects.filter(Q(uf__id=uf_pk) & Q(id=pk))
        data = MunicipioSerializer(municipio,many=True).data
        return Response(data)

# Views que retorna os CasosSuspeitos por data, evolução pontual
class MunicipioCasosSuspeitosLineChartDetail(APIView):
    def get(self,request, uf_pk, pk):
        municipio = Municipio.objects.filter(Q(uf__id=uf_pk) & Q(id=pk)).first()
        registros_c_list = municipio.registodecasossuspeitos_set.all().values_list('created','quantidade').order_by('created')
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
                    "backgroundColor": '#f87979',
                    "pointBackgroundColor": 'white',
                    "borderWidth": 1,
                    "pointBorderColor": '#249EBF',
                    "data": data,
                }
            ]
            }
        }
        return Response(data)

# Views que retorna os casos confirmados por data, evolução pontual
class MunicipioCasosConfirmadosLineChartDetail(APIView):
    def get(self,request, uf_pk, pk):
        municipio = Municipio.objects.filter(Q(uf__id=uf_pk) & Q(id=pk)).first()
        registros_c_list = municipio.registodecasoconfirmado_set.all().values_list('created').annotate(count=Count('id')).order_by('created')
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
                    "backgroundColor": '#f87979',
                    "pointBackgroundColor": 'white',
                    "borderWidth": 1,
                    "pointBorderColor": '#249EBF',
                    "data": data,
                }
            ]
            }
        }
        return Response(data)

# Views que retorna os casos confirmados por data, evolução acumulada
class MunicipioCasosConfirmadosAcumaldoLineChartDetail(APIView):
    def get(self,request, uf_pk, pk):
        municipio = Municipio.objects.filter(Q(uf__id=uf_pk) & Q(id=pk)).first()
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

        data = {
            "datacollection": {
            "labels": labels,
            "datasets": [
                {
                    "label": 'Casos Confirmados',
                    "backgroundColor": '#f87979',
                    "pointBackgroundColor": 'white',
                    "borderWidth": 1,
                    "pointBorderColor": '#249EBF',
                    "data": data,
                }
            ]
            }
        }
        return Response(data)

class MunicipioCasosConfirmadosGruposPopulacionalHBarChartDetail(APIView):
    def get(self,request, uf_pk, pk):
        municipio = Municipio.objects.filter(Q(uf__id=uf_pk) & Q(id=pk)).first()
        labels = []
        data_1 = []
        data_2 = [
            -municipio.populacao_00_04,
            -municipio.populacao_05_09,
            -municipio.populacao_10_14,
            -municipio.populacao_15_19,
            -municipio.populacao_20_24,
            -municipio.populacao_25_29,
            -municipio.populacao_30_39,
            -municipio.populacao_40_49,
            -municipio.populacao_50_59,
            -municipio.populacao_60_69,
            -municipio.populacao_70,
        ]

        for r in range(1,12):
            labels.append(municipio.GRUPO_POPULACIONAL[str(r)])
            data_empty = municipio.registodecasoconfirmado_set.filter(grupo_populacional=r).count()
            data_1.append(data_empty)

        data = {
            "datacollection": {
            "labels": labels,
            "datasets": [
                {
                    "label": 'População por Grupo Etario',
                    "backgroundColor": '#f87979',
                    "pointBackgroundColor": 'white',
                    "borderWidth": 1,
                    "pointBorderColor": '#249EBF',
                    "data": data_2,
                },
                {
                    "label": 'População por Grupo Etario Infectada',
                    "backgroundColor": '#f87979',
                    "pointBackgroundColor": 'white',
                    "borderWidth": 1,
                    "pointBorderColor": '#249EBF',
                    "data": data_1,
                }
            ]
            }
        }
        return Response(data)   

# Views que retorna os Casos de Obitos por data, evolução pontual
class MunicipioCasosObitosLineChartDetail(APIView):
    def get(self,request, uf_pk, pk):
        municipio = Municipio.objects.filter(Q(uf__id=uf_pk) & Q(id=pk)).first()
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
                    "backgroundColor": '#f87979',
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
    def get(self,request, uf_pk, pk):
        municipio = Municipio.objects.filter(Q(uf__id=uf_pk) & Q(id=pk)).first()
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
                    "backgroundColor": '#f87979',
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
    def get(self,request, uf_pk, pk):
        municipio = Municipio.objects.filter(Q(uf__id=uf_pk) & Q(id=pk)).first()
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
                    "backgroundColor": '#f87979',
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
    def get(self,request, uf_pk, pk):
        municipio = Municipio.objects.filter(Q(uf__id=uf_pk) & Q(id=pk)).first()
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
                    "backgroundColor": '#f87979',
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
    def get(self,request, uf_pk, pk):
        municipio = Municipio.objects.filter(Q(uf__id=uf_pk) & Q(id=pk)).first()
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
                    "backgroundColor": '#f87979',
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
    def get(self,request, uf_pk, pk):
        municipio = Municipio.objects.filter(Q(uf__id=uf_pk) & Q(id=pk)).first()
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
                    "backgroundColor": '#f87979',
                    "pointBackgroundColor": 'white',
                    "borderWidth": 1,
                    "pointBorderColor": '#249EBF',
                    "data": data,
                }
            ]
            }
        }
        return Response(data)


class UFList(APIView):
    def get(self,request):
        ufs = UF.objects.all()
        data = UFSerializer(ufs,many=True).data
        return Response(data)

class UFPanoramaDatasList(APIView):
    pass

class UFPanoramaChartCasosSuspeitosList(APIView):
    pass

class UFPanoramaChartCasosConfirmadosList(APIView):
    pass


#Exemplo Class
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = {
            "labels": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "data": [12, 19, 3, 5, 2, 3, 10],
        }   

        return Response(data)