from rest_framework import serializers
from .models import Categoriaalimento

class CategoriaalimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoriaalimento
        fields = '__all__'