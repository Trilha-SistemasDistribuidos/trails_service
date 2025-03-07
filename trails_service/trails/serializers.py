# booking/serializers.py
from rest_framework import serializers
from .models import Trail
from .utils.trail_api_client import get_category  # Função que busca a categoria via API
from .utils.trail_api_client import get_users # Função que busca o usuário via API

class TrailSerializer(serializers.ModelSerializer):
    category_details = serializers.SerializerMethodField()  # Campo customizado
    user_details = serializers.SerializerMethodField()  # Campo customizadocategory_details = serializers.SerializerMethodField()  # Campo customizado

    class Meta:
        model = Trail
        fields = ['id', 'name', 'description', 'user_id', 'user_details', 'location', 'difficulty', 'length_km', 'category_id', 'category_details', 'date_time', 'image']  # Inclui os detalhes
    
    def validate_category_id(self, value):
        # Verifica se a categoria existe antes de criar a review
        if not get_category(value):
            raise serializers.ValidationError("Categoria não encontrada")
        return value

    def get_category_details(self, obj):
        return get_category(obj.category_id)  # Busca os dados da categoria via API
    
    def validate_user_id(self, value):
        if not get_users(value):
            raise serializers.ValidationError("Usuário não encontrado")
        return value
    
    def get_user_details(self, obj):
        return get_users(obj.user_id)  # Campo correto: user_id