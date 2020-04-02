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

        #Todos os dados para gráficos seguem o padrão do Chartjs.
        #Casos Suspeitos
        path('municipio/<int:pk>/casos_suspeitos_line_chart', 
                views.MunicipioCasosSuspeitosLineChartDetail.as_view(), 
                name='municipio_casos_suspeitos_line_chart_detail'),
        
        # Casos Confirmados
        path('municipio/<int:pk>/casos_confirmados_line_chart', 
                views.MunicipioCasosConfirmadosLineChartDetail.as_view(), 
                name='municipio_casos_confirmados_line_chart_detail'),

        path('municipio/<int:pk>/casos_confirmados_acumulado_line_chart', 
                views.MunicipioCasosConfirmadosAcumaldoLineChartDetail.as_view(), 
                name='municipio_casos_confirmados_acumulado_line_chart_detail'),

        path('municipio/<int:pk>/casos_confirmados_grupo_populacional_hbar_chart', 
                views.MunicipioCasosConfirmadosGruposPopulacionalHBarChartDetail.as_view(), 
                name='municipio_casos_confirmados_grupo_populacional_hbar_chart_detail'),
        
        # Casos de Obitos
        path('municipio/<int:pk>/casos_obitos_line_chart', 
                views.MunicipioCasosObitosLineChartDetail.as_view(), 
                name='municipio_casos_obitos_line_chart_detail'),

        path('municipio/<int:pk>/casos_obitos_acumulado_line_chart', 
                views.MunicipioCasosObitosAcumaldoLineChartDetail.as_view(), 
                name='municipio_casos_obitos_acumulado_line_chart_detail'),

        # Casos Curados
        path('municipio/<int:pk>/casos_curados_line_chart', 
                views.MunicipioCasosCuradosLineChartDetail.as_view(), 
                name='municipio_casos_curados_line_chart_detail'),

        path('municipio/<int:pk>/casos_curados_acumulado_line_chart', 
                views.MunicipioCasosCuradosAcumaldoLineChartDetail.as_view(), 
                name='municipio_casos_curados_acumulado_line_chart_detail'),

        #Casos Graves
        path('municipio/<int:pk>/casos_graves_line_chart', 
                views.MunicipioCasosGravesLineChartDetail.as_view(), 
                name='municipio_casos_graves_line_chart_detail'),

        #Retorna os dados para montar o gráfico de casos graves com valores
        # acumulados de um municipios.
        path('municipio/<int:pk>/casos_graves_acumulado_line_chart', 
                views.MunicipioCasosGravesAcumaldoLineChartDetail.as_view(), 
                name='municipio_casos_graves_acumulado_line_chart_detail'),

        #Retorna todos os casos curados de um municipio
        path('municipio/<int:m_pk>/registros_casos_graves', 
                views.MunicipioRegistrosDeCasosGravesList.as_view(), 
                name='municipio_registros_casos_graves_list'),

        #Retorna todos os casos graves de um municipio
        path('municipio/<int:m_pk>/registros_casos_curados', 
                views.MunicipioRegistrosDeCasosCuradosList.as_view(), 
                name='municipio_registros_casos_curados_list'),

        #Retorna todos os casos obitos de um municipio
        path('municipio/<int:m_pk>/registros_casos_obitos', 
                views.MunicipioRegistrosDeCasosObitosList.as_view(), 
                name='municipio_registros_casos_obitos_list'),

        #Retorna todos os casos confrimados de um municipio
        path('municipio/<int:m_pk>/registros_casos_confirmados', 
                views.MunicipioRegistrosDeCasosConfirmadosList.as_view(), 
                name='municipio_registros_casos_confirmados_list'),

        #Retorna todos os casos suspeitos de um municipio
        path('municipio/<int:m_pk>/registros_casos_suspeitos', 
                views.MunicipioRegistrosDeCasosSuspeitosList.as_view(), 
                name='municipio_registros_casos_suspeitos_list'),
        
        #Retorna os dados detalhados de um municipio
        path('municipio/<int:pk>', 
                views.MunicipioPanoramaDataDetail.as_view(), 
                name='municipio_detail'), 

        #Retorna lista com todos os municipios
        path('municipios/', 
                views.MunicipiosList.as_view(), 
                name='municipios_list'),

        path('ibge_grupos_populacionais/', 
                views.IBGEGruposPopulacionais.as_view(), 
                name='ibge_grupos_populacionais'),

        #Retorna lista com todos os estados
        path('ufs/', 
                views.UFList.as_view(), 
                name='ufs_list'),
         
]