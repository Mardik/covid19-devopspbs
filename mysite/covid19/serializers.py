from rest_framework import serializers

from .models import *

class RegistoDeCasoGraveSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistoDeCasoGrave
        fields = '__all__'

class RegistoDeCasoCuradoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistoDeCasoCurado
        fields = '__all__'

class RegistoDeCasoObitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistoDeCasoObito
        fields = '__all__'

class RegistoDeCasoConfirmadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistoDeCasoConfirmado
        fields = '__all__'

class RegistoDeCasosSuspeitosSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistoDeCasosSuspeitos
        fields = '__all__'    

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = (
            'id',
            'nome',
            'uf',
            'populacao_total',
            'populacao_projetada',
            'populacao_idosos',
            'populacao_adultos',
            'populacao_jovens',
            'populacao_infantil',
            'populacao_00_04',
            'populacao_05_09',
            'populacao_10_14',
            'populacao_15_19',
            'populacao_20_24',
            'populacao_25_29',
            'populacao_30_39',
            'populacao_40_49',
            'populacao_50_59',
            'populacao_60_69',
            'populacao_70',
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
            'populacao_sob_suspeita_total',
            'populacao_curada_total',
            'populacao_obito_total',
        )

class UFSerializer(serializers.ModelSerializer):
    municipios = MunicipioSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = UF
        fields = '__all__'