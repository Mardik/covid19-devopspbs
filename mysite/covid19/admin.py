from django.contrib import admin
from .models import *


#Admin classes
#Admin Classe Tabular inline para exibição tabular em linha
#do form para adição de rgistro de casos suspeitos.
# Organização tabular inline do form Instituições de Saúde
#Admin classe do model Municipio contemplando a exição tabular para
#registro de casos supeitos e excluindo o campo registros de casos supeitos
#do change form.

class RegistoDeCasoConfirmadoAdmin(admin.ModelAdmin):
    list_display = [
        'municipio',
        'sexo',
        'grupo_populacional',
        'created',
    ]
    list_filter = [
        'municipio__nome'
    ]
    raw_id_fields = [('municipio')]

class RegistoDeCasosSuspeitosAdmin(admin.ModelAdmin):
    list_display = [
        'municipio',
        'quantidade',
        'created',
    ]
    list_filter = [
        'municipio__nome'
    ]
    raw_id_fields = [('municipio')]

class MunicipioAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = [
        'uf',
        'nome',
        'populacao_total',
        'populacao_idosos',
        'populacao_adultos',
        'populacao_jovens',
        'populacao_infantil',
    ]
    readonly_fields = (
        'id',
        'populacao_total',
        'populacao_projetada',
        'populacao_idosos',
        'populacao_adultos',
        'populacao_jovens',
        'populacao_infantil',
        'populacao_total_infectada',
        'populacao_idosos_infectada',
        'populacao_adultos_infectada',
        'populacao_jovens_infectada',
        'populacao_infantil_infectada',
        'populacao_00_04_infectada',
        'populacao_05_09_infectada',
        'populacao_10_14_infectada',
        'populacao_15_19_infectada',
        'populacao_20_24_infectada',
        'populacao_25_29_infectada',
        'populacao_30_39_infectada',
        'populacao_40_49_infectada',
        'populacao_50_59_infectada',
        'populacao_60_69_infectada',
        'populacao_70_infectada',
    )
    list_filter = [
        'uf__sigla'
    ]
    exclude = (
        'registroDeCasosSuspeitos',
        'registroDeCasosConfirmados',
        'registroDeCasosGraves',
        'registroDeCasosObitos',
        'registroDeCasosCurados',
        'instituicoesDeSaude',
        'bairros',
    )
class UFAdmin(admin.ModelAdmin):
    readonly_fields = (
        'id',
    )
    list_display = [
        'id','sigla','nome'
    ]

#Admin Register
admin.site.register(UF,UFAdmin)
admin.site.register(Municipio,MunicipioAdmin)
admin.site.register(Bairro)
admin.site.register(InstituicaoDeSaude)
admin.site.register(RegistoDeCasoConfirmado,RegistoDeCasoConfirmadoAdmin)
admin.site.register(RegistoDeCasosSuspeitos,RegistoDeCasosSuspeitosAdmin)
admin.site.register(RegistoDeCasoObito)
admin.site.register(RegistoDeCasoCurado)
admin.site.register(RegistoDeCasoGrave)
admin.site.register(RegistoDeRecursosEmSaude)