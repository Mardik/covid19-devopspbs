from . import views
from django.urls import path

urlpatterns = [
    path('home', views.HomePageView.as_view(), name='home'),
    path('', views.IndexPageView.as_view(), name='index'),
    path('ufs/', views.UFList.as_view(), name='ufs_list'),
    path('uf/<int:uf_pk>/municipio/<int:pk>', views.MunicipioPanoramaDataDetail.as_view(), name='uf_municipio_detail'),
    path('municipios/', views.MunicipiosList.as_view(), name='ufs_list'),    
    path('api/chart/data/', views.ChartData.as_view()),
]