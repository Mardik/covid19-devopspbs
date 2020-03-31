from rest_framework import serializers

from .models import *

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
            #'populacao_infectada_acumulado_diaria',
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
            #'populacao_curada_acumulado_diario',
            'populacao_curada_total',
            #'populacao_obito_acumulado_diario',
            'populacao_obito_total',
        )

class UFSerializer(serializers.ModelSerializer):
    municipios = MunicipioSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = UF
        fields = '__all__'