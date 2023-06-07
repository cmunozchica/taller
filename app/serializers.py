from rest_framework import serializers
from .models import RepuestoTaller

class RepuestoSerializer(serializers.ModelSerializer):
    numero_parte = serializers.CharField(source = 'numparte.numero_parte')
    

    class Meta:
        model = RepuestoTaller
        fields = '__all__'


class ListSerializer(serializers.ModelSerializer):
    owner = RepuestoSerializer(read_only=True)
    ownerId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=RepuestoTaller.objects.all(), source='owner')
    
    class Meta:
        model = RepuestoTaller
        fields = ('id', 'title', 'body', 'owner', 'ownerId', 'comments')