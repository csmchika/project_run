from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Run

class AthleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'last_name', 'first_name',]


class RunSerializer(serializers.ModelSerializer):
    athlete_data = AthleteSerializer(source="athlete", read_only=True)
    class Meta:
        model = Run
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    runs_finished = serializers.IntegerField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'date_joined', 'username', 'last_name', 'first_name', 'type', 'runs_finished']


    # Определяем метод, который вычисляет значение поля
    def get_type(self, obj):
        is_staff = obj.is_staff
        return "coach" if is_staff else "athlete"

    # def get_runs_finished(self, obj):
    #     return obj.athletes.filter(status='finished').count()