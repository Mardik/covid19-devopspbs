from django.db import models
from django.utils import timezone

#Registo de Casos Suspeitos
class RegistoDeCasosSuspeitos(models.Model):
    #Listas

    #Atributos do Model
    quantidade = models.IntegerField(verbose_name='Quantidade de casos suspeitos no momento:')
    created = models.DateField(default=timezone.now, verbose_name='Data de Cadastro:')
    #Atributos de Relacionamentos
    municipio = models.ForeignKey('Municipio', verbose_name='Municipio:',on_delete=models.PROTECT)
    #Metodos

    #Meta dados
    class Meta:
        verbose_name = 'Registro de Casos Suspeitos'
        verbose_name_plural = 'Registro de Casos Suspeitos'

    #Representação textual
    def __str__(self):
        return "%s - %s / %s" % (self.municipio.uf.sigla,self.municipio.nome, self.created)

#Registo de Casos Confirmados
class RegistoDeCasoConfirmado(models.Model):
    #Listas
    GRUPO_POPULACIONAL = [
        (1,'populacao_00_04'),
        (2,'populacao_05_09'),
        (3,'populacao_10_14'),
        (4,'populacao_15_19'),
        (5,'populacao_20_24'),
        (6,'populacao_25_29'),
        (7,'populacao_30_39'),
        (8,'populacao_40_49'),
        (9,'populacao_50_59'),
        (10,'populacao_60_69'),
        (11,'populacao_70'),
    ]

    SEXO = [
        (2,'desconhecido'),
        (1,'feminino'),
        (0,'masculino')
    ]

    #Atributos do Model
    grupo_populacional = models.IntegerField(choices=GRUPO_POPULACIONAL, default=0)
    sexo = models.IntegerField(choices=SEXO, default=0)
    created = models.DateField(default=timezone.now, verbose_name='Data de Cadastro:')
    #Atributos de Relacionamentos
    municipio = models.ForeignKey('Municipio', verbose_name='Municipio:',on_delete=models.PROTECT)
    #Metodos

    #Meta dados
    class Meta:
        verbose_name = 'Registro de Caso Confirmado'
        verbose_name_plural = 'Registros de Casos Confirmados'

    #Representação textual
    def __str__(self):
        return "%s - %s / %s" % (self.municipio.uf.sigla,self.municipio.nome, self.created)

#Registo de Casos Obitos
class RegistoDeCasoObito(models.Model):
    #Listas
    GRUPO_POPULACIONAL = [
        (1,'populacao_00_04'),
        (2,'populacao_05_09'),
        (3,'populacao_10_14'),
        (4,'populacao_15_19'),
        (5,'populacao_20_24'),
        (6,'populacao_25_29'),
        (7,'populacao_30_39'),
        (8,'populacao_40_49'),
        (9,'populacao_50_59'),
        (10,'populacao_60_69'),
        (11,'populacao_70'),
    ]

    SEXO = [
        (2,'desconhecido'),
        (1,'feminino'),
        (0,'masculino')
    ]

    #Atributos do Model
    grupo_populacional = models.IntegerField(choices=GRUPO_POPULACIONAL, default=0)
    sexo = models.IntegerField(choices=SEXO, default=0)
    created = models.DateField(default=timezone.now, verbose_name='Data de Cadastro:')
    #Atributos de Relacionamentos
    municipio = models.ForeignKey('Municipio', verbose_name='Municipio:',on_delete=models.PROTECT)

    #Meta dados
    class Meta:
        verbose_name = 'Registro de Caso Obito'
        verbose_name_plural = 'Registros de Casos Obitos'

    #Representação textual
    def __str__(self):
         return "%s - %s / %s" % (self.municipio.uf.sigla,self.municipio.nome, self.created)

#Registo de Casos Curados
class RegistoDeCasoCurado(models.Model):
    #Listas

    GRUPO_POPULACIONAL = [
        (1,'populacao_00_04'),
        (2,'populacao_05_09'),
        (3,'populacao_10_14'),
        (4,'populacao_15_19'),
        (5,'populacao_20_24'),
        (6,'populacao_25_29'),
        (7,'populacao_30_39'),
        (8,'populacao_40_49'),
        (9,'populacao_50_59'),
        (10,'populacao_60_69'),
        (11,'populacao_70'),
    ]

    SEXO = [
        (2,'desconhecido'),
        (1,'feminino'),
        (0,'masculino')
    ]

    #Atributos do Model
    grupo_populacional = models.IntegerField(choices=GRUPO_POPULACIONAL, default=0)
    sexo = models.IntegerField(choices=SEXO, default=0)
    created = models.DateField(default=timezone.now, verbose_name='Data de Cadastro:')
    #Atributos de Relacionamentos
    municipio = models.ForeignKey('Municipio', verbose_name='Municipio:',on_delete=models.PROTECT)
    #Metodos

    #Meta dados
    class Meta:
        verbose_name = 'Registro de Caso de Curado:'
        verbose_name_plural = 'Registros de Casos de Curas:'

    #Representação textual
    def __str__(self):
         return "%s - %s / %s" % (self.municipio.uf.sigla,self.municipio.nome, self.created)

#Registo de Casos Graves
class RegistoDeCasoGrave(models.Model):
    #Listas
    GRUPO_POPULACIONAL = [
        (1,'populacao_00_04'),
        (2,'populacao_05_09'),
        (3,'populacao_10_14'),
        (4,'populacao_15_19'),
        (5,'populacao_20_24'),
        (6,'populacao_25_29'),
        (7,'populacao_30_39'),
        (8,'populacao_40_49'),
        (9,'populacao_50_59'),
        (10,'populacao_60_69'),
        (11,'populacao_70'),
    ]

    SEXO = [
        (2,'desconhecido'),
        (1,'feminino'),
        (0,'masculino')
    ]

    #Atributos do Model
    grupo_populacional = models.IntegerField(choices=GRUPO_POPULACIONAL, default=0)
    sexo = models.IntegerField(choices=SEXO, default=0)
    created = models.DateField(default=timezone.now, verbose_name='Data de Cadastro:')
    #Atributos de Relacionamentos
    municipio = models.ForeignKey('Municipio', verbose_name='Municipio:',on_delete=models.PROTECT)
    #Metodos

    #Meta dados
    class Meta:
        verbose_name = 'Registro de Caso Grave'
        verbose_name_plural = 'Registros de Casos Graves'

    #Representação textual
    def __str__(self):
        return "%s - %s / %s" % (self.municipio.uf.sigla,self.municipio.nome, self.created)

#Registo de Recursos em Saúde
class RegistoDeRecursosEmSaude(models.Model):    

    #Listas
    TIPO_DE_RECURSO = [
        (0,'LEITO COVID-19'),
    ]
    #Atributos do Model
    tipo_de_recurso = models.IntegerField(choices=TIPO_DE_RECURSO, default=0)
    quantidade_total = models.IntegerField(verbose_name='Quantidade Total do Recurso:')
    quantidade_disponivel = models.IntegerField(verbose_name='Quantidade do Recurso Disponivel no Momento:')
    created = models.DateTimeField(default=timezone.now, verbose_name='Data de Registro:')
    #Atributos de Relacionamentos
    instituicao = models.ForeignKey('InstituicaoDeSaude', verbose_name='Instituição de Saúde:',on_delete=models.PROTECT)

    #Metodos

    #Meta dados
    class Meta:
        verbose_name = 'Registro de Recurso em Saúde'
        verbose_name_plural = 'Registros de Recursos em Saúde'

    #Representação textual
    def __str__(self):
        return "%s - %s - %s - %s / %s - %s" % (
                                    self.instituicao.municipio.uf.sigla, 
                                    self.instituicao.municipio.nome,
                                    self.instituicao.nome,
                                    self.quantidade_total, 
                                    self.quantidade_disponivel,
                                    self.created,
                                )

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
    endereço = models.CharField(max_length=150, verbose_name='Endereço:')
    #Atributos de Relacionamentos
    municipio = models.ForeignKey('Municipio', verbose_name='Municipio:',on_delete=models.PROTECT)
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
    #Static datas
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
    #Listas

    #Atributos do Model
    nome = models.CharField(max_length=100, verbose_name='Nome:')
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
    #Metodos

    #Métodos caculated fields sobre a população em geral
        
    @property
    def populacao_idosos(self):
        return (self.populacao_60_69 + 
                self.populacao_70)
        
    @property
    def populacao_adultos(self):
        return (self.populacao_20_24+
                self.populacao_25_29+
                self.populacao_30_39+
                self.populacao_40_49+
                self.populacao_50_59)
        
    @property
    def populacao_jovens(self):
        return  (self.populacao_10_14+ 
                self.populacao_15_19)
        
    @property
    def populacao_infantil(self):
        return (self.populacao_00_04+ 
                self.populacao_05_09)

    @property
    def populacao_total(self):
        return (
                self.populacao_00_04+ 
                self.populacao_05_09+
                self.populacao_10_14+ 
                self.populacao_15_19+  
                self.populacao_20_24+
                self.populacao_25_29+
                self.populacao_30_39+
                self.populacao_40_49+
                self.populacao_50_59+
                self.populacao_60_69+ 
                self.populacao_70
            )

    #Métodos calculated fiedls sobre a população infectada
        
    @property
    def populacao_00_04_infectada(self):
        return self.registodecasoconfirmado_set.all().filter(grupo_populacional=1).count()
        
    @property
    def populacao_05_09_infectada(self):
        return self.registodecasoconfirmado_set.all().filter(grupo_populacional=2).count()
        
    @property
    def populacao_10_14_infectada(self):
        return self.registodecasoconfirmado_set.all().filter(grupo_populacional=3).count()
        
    @property
    def populacao_15_19_infectada(self):
        return self.registodecasoconfirmado_set.all().filter(grupo_populacional=4).count()
        
    @property
    def populacao_20_24_infectada(self):
        return self.registodecasoconfirmado_set.all().filter(grupo_populacional=5).count()
        
    @property
    def populacao_25_29_infectada(self):
        return self.registodecasoconfirmado_set.all().filter(grupo_populacional=6).count()
        
    @property
    def populacao_30_39_infectada(self):
        return self.registodecasoconfirmado_set.all().filter(grupo_populacional=7).count()
        
    @property
    def populacao_40_49_infectada(self):
        return self.registodecasoconfirmado_set.all().filter(grupo_populacional=8).count()
        
    @property
    def populacao_50_59_infectada(self):
        return self.registodecasoconfirmado_set.all().filter(grupo_populacional=9).count()
    
    @property
    def populacao_60_69_infectada(self):
        return self.registodecasoconfirmado_set.all().filter(grupo_populacional=10).count()
    
    @property
    def populacao_70_infectada(self):
        return self.registodecasoconfirmado_set.all().filter(grupo_populacional=11).count()

    @property        
    def populacao_idosos_infectada(self):
        return (
                self.populacao_60_69_infectada + 
                self.populacao_70_infectada
                )

    @property
    def populacao_adultos_infectada(self):
        return (
                self.populacao_20_24_infectada+
                self.populacao_25_29_infectada+
                self.populacao_30_39_infectada+
                self.populacao_40_49_infectada+
                self.populacao_50_59_infectada
                )

    @property
    def populacao_jovens_infectada(self):
        return  (
                self.populacao_10_14_infectada+ 
                self.populacao_15_19_infectada
                )

    @property
    def populacao_infantil_infectada(self):
        return (
                self.populacao_00_04_infectada+ 
                self.populacao_05_09_infectada
                )
    
    @property
    def populacao_infectada_acumulado_diaria(self):
        return self.registodecasoconfirmado_set.all().count()

    @property
    def populacao_total_infectada(self):
        return self.registodecasoconfirmado_set.all().count()

    #Métodos calculated fields sobre a população sob suspeita
    @property
    def populacao_sob_suspeita_total(self):
        return self.registodecasossuspeitos_set.all().count() 
    
    #Método calculated fields sobre a população recuperada/curada
    @property
    def populacao_curada_acumulado_diario(self):
        return self.registodecasocurado_set.all().count()

    @property
    def populacao_curada_total(self):
        return self.registodecasocurado_set.all().count()
    
    # Peço desculpas pela, mais foi a melhor referânecia que encontrei.
    #Método calculated fields sobre a população que veio a obito.
    @property
    def populacao_obito_acumulado_diario(self):
        return self.registodecasoobito_set.all().count()

    @property
    def populacao_obito_total(self):
        return self.registodecasoobito_set.all().count()

    #Métodos calculated fields sobe a população em geral infectada
    # baeado no modelo SIR
        
    @property
    def populacao_susceptiveis(self):
        pass
        
    @property
    def populacao_infecciosos(self):
        pass
    
    @property
    def populacao_removidos(self):
        pass

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