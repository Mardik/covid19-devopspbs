from random import randint
from django.db.models import Q
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from  .serializers import *
# Create your views here.

class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'covid19/charts.html')

class IndexPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'covid19/index.html')

class MunicipiosList(APIView):
    def get(self,request):
        municipios = Municipio.objects.all()
        data = MunicipioSerializer(municipios,many=True).data
        return Response(data)


class MunicipioPanoramaDataDetail(APIView):
    def get(self,request, uf_pk, pk):
        municipio = Municipio.objects.filter(Q(uf__id=uf_pk) & Q(id=pk))
        dados_gerais = list(municipio.values(
                    'uf__id',
                    'uf__nome',
                    'id',
                    'nome',
                    'populacao_total',
                    'populacao_projetada',
                    ))[0]

        dados_epidemiologicos_gerais = {
            "populacao_infectada_total" : municipio.populacao_infectada_total,
            "populacao_curada_total" : municipio.populacao_curada_total,
            "populacao_obito_total" : municipio.populacao_obito_total,
            "populacao_sob_suspeita_total" : municipio.populacao_sob_suspeita_total,
        }

        data = {"results": {
            "municipio" :{
                "dados_gerais": dados_gerais,
                "dados_epidemiologicos_gerais" : dados_epidemiologicos_gerais,
            }
        }}
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