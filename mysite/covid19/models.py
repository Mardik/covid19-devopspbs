from django.db import models
from django.utils import timezone

#Registo de Casos Suspeitos
class RegistoDeCasosSuspeitos(models.Model):
    #Listas

    #Atributos do Model
    quantidade = models.IntegerField(verbose_name='Quantidade de novos casos:')
    created = models.DateTimeField(default=timezone.now, verbose_name='Data de Cadastro:')
    #Atributos de Relacionamentos

    #Metodos

    #Meta dados
    class Meta:
        verbose_name = 'Registro de Casos Suspeitos'
        verbose_name_plural = 'Registros de Casos Suspeitos'

    #Representação textual
    def __str__(self):
        return "%s / %s" % (self.quantidade, self.created)

#Registo de Casos Confirmados
class RegistoDeCasosConfirmados(models.Model):
    #Listas

    #Atributos do Model
    quantidade = models.IntegerField(verbose_name='Quantidade de novos caso:')
    created = models.DateTimeField(default=timezone.now, verbose_name='Data de Cadastro:')
    #Atributos de Relacionamentos

    #Metodos

    #Meta dados
    class Meta:
        verbose_name = 'Registro de Casos Confirmados'
        verbose_name_plural = 'Registros de Casos Confirmados'

    #Representação textual
    def __str__(self):
        return "%s / %s" % (self.quantidade, self.created)

#Registo de Casos Obitos
class RegistoDeCasosObitos(models.Model):
    #Listas

    #Atributos do Model
    quantidade = models.IntegerField(verbose_name='Quantidade de novos caso:')
    created = models.DateTimeField(default=timezone.now, verbose_name='Data de Cadastro:')
    #Atributos de Relacionamentos

    #Metodos

    #Meta dados
    class Meta:
        verbose_name = 'Registro de Casos Obitos'
        verbose_name_plural = 'Registros de Casos Obitos'

    #Representação textual
    def __str__(self):
        return "%s / %s" % (self.quantidade, self.created)

#Registo de Casos Curados
class RegistoDeCasosCurados(models.Model):
    #Listas

    #Atributos do Model
    quantidade = models.IntegerField(verbose_name='Quantidade de novos caso:')
    created = models.DateTimeField(default=timezone.now, verbose_name='Data de Cadastro:')
    #Atributos de Relacionamentos

    #Metodos

    #Meta dados
    class Meta:
        verbose_name = 'Registro de Casos Curados'
        verbose_name_plural = 'Registros de Casos Curados'

    #Representação textual
    def __str__(self):
        return "%s / %s" % (self.quantidade, self.created)

#Registo de Casos Graves
class RegistoDeCasosGraves(models.Model):
    #Listas

    #Atributos do Model
    quantidade = models.IntegerField(verbose_name='Quantidade de novos caso:')
    created = models.DateTimeField(default=timezone.now, verbose_name='Data de Cadastro:')
    #Atributos de Relacionamentos

    #Metodos

    #Meta dados
    class Meta:
        verbose_name = 'Registro de Casos Graves'
        verbose_name_plural = 'Registros de Casos Graves'

    #Representação textual
    def __str__(self):
        return "%s / %s" % (self.quantidade, self.created)
"""
#Registo Populacional
class RegistoPopulacional(models.Model):
    #Listas

    #Atributos do Model
    populacao_total = models.BigIntegerField()
    populacao_grupo_de_risco = models.BigIntegerField()
    populacao_idosos = models.BigIntegerField()
    populacao_adultos = models.BigIntegerField()
    populacao_jovens = models.BigIntegerField()
    populacao_infantil = models.BigIntegerField()

    #Atributos de Relacionamentos

    #Metodos

    #Meta dados
    class Meta:
        verbose_name = 'Registro Populacional'
        verbose_name_plural = 'Registros de Populacionais'

    #Representação textual
    def __str__(self):
        return "Registro Populacional"
"""

#Registo de Recursos em Saúde
class RegistoDeRecursosEmSaude(models.Model):
    #Listas
    TIPO_DE_RECURSO = [
        (0,'LEITO COVID-19'),
    ]
    #Atributos do Model
    tipo_de_recurso = models.IntegerField(choices=TIPO_DE_RECURSO, default=0)
    quantidade = models.IntegerField()
    created = models.DateTimeField(default=timezone.now, verbose_name='Data de Registro:')
    #Atributos de Relacionamentos

    #Metodos

    #Meta dados
    class Meta:
        verbose_name = 'Registro de Recurso em Saúde'
        verbose_name_plural = 'Registros de Recursos em Saúde'

    #Representação textual
    def __str__(self):
        return "%s - %s / %s" % (self.municipio ,self.quantidade, self.created)

#Instituições de Saúde
class InstituicaoDeSaude(models.Model):
    #Listas
    TIPO_DE_INSTITUICAO =(
        (0,'publica'),
        (1,'privada'),
    )
    #Atributos do Model
    nome = models.CharField(max_length=200, verbose_name='Nome:')
    tipo_de_instituicao = models.IntegerField(choices=TIPO_DE_INSTITUICAO, default=0)
    bairro = models.ForeignKey('Bairro', verbose_name='Bairro:',on_delete=models.PROTECT)
    endereço = models.CharField(max_length=150, verbose_name='Endereço:')
    #Atributos de Relacionamentos
    registrosDeRecursos = models.ManyToManyField(RegistoDeRecursosEmSaude)
    #Metodos

    #Meta dados
    class Meta:
        verbose_name = 'Instituição de Saúde'
        verbose_name_plural = 'Instituições de Saúde'

    #Representação textual
    def __str__(self):
        return "%s - %s" % (self.municipio ,self.nome)

class Bairro(models.Model):
    #Atributos
    nome = models.CharField(max_length=50, verbose_name='Nome:',blank=True)
    #Metodos

    #Meta dados
    class Meta:
        verbose_name = 'Bairro'
        verbose_name_plural = 'Bairros'

    #Representação textual
    def __str__(self):
        return "%s" % (self.nome)


#Unidade da Municipio
class Municipio(models.Model):
    #Listas

    #Atributos do Model
    nome = models.CharField(max_length=100, verbose_name='Nome:')
    populacao_total = models.BigIntegerField(default=0)
    populacao_projetada = models.BigIntegerField(default=0)
    populacao_00_04 = models.BigIntegerField(default=0)
    populacao_05_09 = models.BigIntegerField(default=0)
    populacao_10_14 = models.BigIntegerField(default=0)
    populacao_15_19 = models.BigIntegerField(default=0)
    populacao_20_24 = models.BigIntegerField(default=0)
    populacao_25_29 = models.BigIntegerField(default=0)
    populacao_30_39 = models.BigIntegerField(default=0)
    populacao_40_49 = models.BigIntegerField(default=0)
    populacao_50_59 = models.BigIntegerField(default=0)
    populacao_60_69 = models.BigIntegerField(default=0)
    populacao_70 = models.BigIntegerField(default=0)
    

    #Atributos de Relacionamentos
    uf = models.ForeignKey('UF', verbose_name='UF:',on_delete=models.PROTECT)
    registroDeCasosSuspeitos = models.ManyToManyField(RegistoDeCasosSuspeitos)
    registroDeCasosConfirmados = models.ManyToManyField(RegistoDeCasosConfirmados)
    registroDeCasosGraves = models.ManyToManyField(RegistoDeCasosGraves)
    registroDeCasosObitos = models.ManyToManyField(RegistoDeCasosObitos)
    registroDeCasosCurados = models.ManyToManyField(RegistoDeCasosCurados)
    instituicoesDeSaude = models.ManyToManyField(InstituicaoDeSaude)
    bairros = models.ManyToManyField(Bairro)
    #Metodos
    #def populacao_grupo_de_risco(self):
    def populacao_idosos(self):
        return populacao_60_69 + populacao_70
    def populacao_adultos(self):
        return (populacao_20_24+
                populacao_25_29+
                populacao_30_39+
                populacao_40_49+
                populacao_50_59)
    def populacao_jovens(self):
        return populacao_10_14+populacao_15_19
    def populacao_infantil(self):
        return populacao_00_04+populacao_05_09

    #Meta dados
    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'

    #Representação textual
    def __str__(self):
        return "%s - %s" % (self.uf.sigla,self.nome)

#Unidade da Federação
class UF(models.Model):

    #Listas

    #Atributos
    nome = models.CharField(max_length=50, verbose_name='Nome:',blank=True)
    sigla = models.CharField(max_length=2, verbose_name='Sigla:',blank=True)
    #Atribuitos de Relacionamentos
    
    #Metodos

    #Meta dados
    class Meta:
        verbose_name = 'Unidade da Feração'
        verbose_name_plural = 'Undiades da Federação'

    #Representação textual
    def __str__(self):
        return "%s - %s" % (self.sigla,self.nome)