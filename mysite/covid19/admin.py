from django.contrib import admin
from .models import *


class InstituicaoDeSaudeRegistrosDeRecursosEmSaudeInline(admin.TabularInline):

    model = InstituicaoDeSaude.registrosDeRecursos.through

class InstituicaoDeSaudeAdmin(admin.ModelAdmin):
    inlines = [
        InstituicaoDeSaudeRegistrosDeRecursosEmSaudeInline,
    ]
    exclude = ('registrosDeRecursos',)

#Admin classes
#Admin Classe Tabular inline para exibição tabular em linha
#do form para adição de rgistro de casos suspeitos.
class MunicipioRegistoDeCasosSuspeitosInline(admin.TabularInline):
    #Referência a Through gerada automaticamente em relacionamentos
    # m2m. 
    model = Municipio.registroDeCasosSuspeitos.through

# Organização tabular inline do form RegistoDeCasosConfirmados
class MunicipioRegistoDeCasosConfirmadosInline(admin.TabularInline):
    model = Municipio.registroDeCasosSuspeitos.through

# Organização tabular inline do form RegistoDeCasosConfirmados
class MunicipioRegistoDeCasosConfirmadosInline(admin.TabularInline):
    model = Municipio.registroDeCasosConfirmados.through

# Organização tabular inline do form RegistoDeCasosObitos
class MunicipioRegistoDeCasosObitosInline(admin.TabularInline):
    model = Municipio.registroDeCasosObitos.through

# Organização tabular inline do form RegistoDeCasosCurados
class MunicipioRegistoDeCasosCuradosInline(admin.TabularInline):
    model = Municipio.registroDeCasosCurados.through

# Organização tabular inline do form RegistoDeCasosGraves
class MunicipioRegistoDeCasosGravesInline(admin.TabularInline):
    model = Municipio.registroDeCasosGraves.through

# Organização tabular inline do form Instituições de Saúde
class MunicipioInstituicaoDeSaudeInline(admin.TabularInline):
    model = Municipio.instituicoesDeSaude.through

# Organização tabular inline do form Bairro
class MunicipioBairrosInline(admin.TabularInline):
    model = Municipio.bairros.through

#Admin classe do model Municipio contemplando a exição tabular para
#registro de casos supeitos e excluindo o campo registros de casos supeitos
#do change form.
class MunicipioAdmin(admin.ModelAdmin):
    inlines = [
        MunicipioInstituicaoDeSaudeInline,
        MunicipioBairrosInline,
        MunicipioRegistoDeCasosSuspeitosInline,
        MunicipioRegistoDeCasosConfirmadosInline,
        MunicipioRegistoDeCasosGravesInline,
        MunicipioRegistoDeCasosObitosInline,
        MunicipioRegistoDeCasosCuradosInline,
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

#Admin Register
admin.site.register(UF)
admin.site.register(Municipio,MunicipioAdmin)
admin.site.register(Bairro)
admin.site.register(InstituicaoDeSaude,InstituicaoDeSaudeAdmin)
admin.site.register(RegistoDeCasosSuspeitos)
admin.site.register(RegistoDeCasosConfirmados)
admin.site.register(RegistoDeCasosObitos)
admin.site.register(RegistoDeCasosCurados)
admin.site.register(RegistoDeCasosGraves)
admin.site.register(RegistoDeRecursosEmSaude)