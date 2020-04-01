from . import views
from django.urls import path
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

API_TITLE = 'Pará | Covid19 API'
API_DESCRIPTION = """
<p>
Está API tem como objetivo, fornecer dados sobre a evolução da infecção provocada 
pelo coronavirus, dados populacionais do IBGE como, população total, projetada,
população por grupos populacionas segredados por idade, além dos dados sobre
instituições de saúde do estado e seus recursos em saúde relevantes.
</p>
<p>
Essa API foi idealizada pela comunidade <a href="https://devopspbs.org/">DevOpsPBS</a>,
mais sinta-se a vontade para da um fork nesse projeto, propor melhoria ou realizar 
pull requests.
</p>
"""

urlpatterns = [
        path('', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),

        path('ufs/', 
                views.UFList.as_view(), 
                name='ufs_list'),

        path('uf/<int:uf_pk>/municipio/<int:pk>', 
                views.MunicipioPanoramaDataDetail.as_view(), 
                name='uf_municipio_detail'),

        #Casos Suspeitos
        path('uf/<int:uf_pk>/municipio/<int:pk>/casos_suspeitos_line_chart', 
                views.MunicipioCasosSuspeitosLineChartDetail.as_view(), 
                name='uf_municipio_casos_suspeitos_line_chart_detail'),
        
        # Casos Confirmados
        path('uf/<int:uf_pk>/municipio/<int:pk>/casos_confirmados_line_chart', 
                views.MunicipioCasosConfirmadosLineChartDetail.as_view(), 
                name='uf_municipio_casos_confirmados_line_chart_detail'),

        path('uf/<int:uf_pk>/municipio/<int:pk>/casos_confirmados_acumulado_line_chart', 
                views.MunicipioCasosConfirmadosAcumaldoLineChartDetail.as_view(), 
                name='uf_municipio_casos_confirmados_acumulado_line_chart_detail'),

        path('uf/<int:uf_pk>/municipio/<int:pk>/casos_confirmados_grupo_populacional_hbar_chart', 
                views.MunicipioCasosConfirmadosGruposPopulacionalHBarChartDetail.as_view(), 
                name='uf_municipio_casos_confirmados_grupo_populacional_hbar_chart_detail'),
        
        # Casos de Obitos
        path('uf/<int:uf_pk>/municipio/<int:pk>/casos_obitos_line_chart', 
                views.MunicipioCasosObitosLineChartDetail.as_view(), 
                name='uf_municipio_casos_obitos_line_chart_detail'),

        path('uf/<int:uf_pk>/municipio/<int:pk>/casos_obitos_acumulado_line_chart', 
                views.MunicipioCasosObitosAcumaldoLineChartDetail.as_view(), 
                name='uf_municipio_casos_obitos_acumulado_line_chart_detail'),

        # Casos Curados
        path('uf/<int:uf_pk>/municipio/<int:pk>/casos_curados_line_chart', 
                views.MunicipioCasosCuradosLineChartDetail.as_view(), 
                name='uf_municipio_casos_curados_line_chart_detail'),

        path('uf/<int:uf_pk>/municipio/<int:pk>/casos_curados_acumulado_line_chart', 
                views.MunicipioCasosCuradosAcumaldoLineChartDetail.as_view(), 
                name='uf_municipio_casos_curados_acumulado_line_chart_detail'),

        #Casos Graves
        path('uf/<int:uf_pk>/municipio/<int:pk>/casos_graves_line_chart', 
                views.MunicipioCasosGravesLineChartDetail.as_view(), 
                name='uf_municipio_casos_graves_line_chart_detail'),

        path('uf/<int:uf_pk>/municipio/<int:pk>/casos_graves_acumulado_line_chart', 
                views.MunicipioCasosGravesAcumaldoLineChartDetail.as_view(), 
                name='uf_municipio_casos_graves_acumulado_line_chart_detail'),

        path('municipios/', 
                views.MunicipiosList.as_view(), 
                name='municipios_list'),    
]