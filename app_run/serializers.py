from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Run

class RunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Run
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'date_joined', 'username', 'last_name', 'first_name', 'type']


    # Определяем метод, который вычисляет значение поля
    def get_type(self, obj):
        is_staff = obj.is_staff
        return "coach" if is_staff else "athlete"

