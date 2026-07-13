from django.db.models import Count, Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.views import APIView

from .models import Run
from .serializers import RunSerializer, UserSerializer
from django.conf import settings


@api_view(['GET'])
def company_details_view(request):
    details = {'company_name': "Забег за пивом",
               'slogan': 'Беги Форест, беги',
               'contacts': 'КБшечка у дома'}
    return Response(details)

class RunPagination(PageNumberPagination):
    page_size_query_param = 'size'

class UserPagination(PageNumberPagination):
    page_size_query_param = 'size'



class RunViewSet(viewsets.ModelViewSet):
    queryset = Run.objects.select_related('athlete').all()
    serializer_class = RunSerializer
    pagination_class = RunPagination


    filter_backends = [DjangoFilterBackend, OrderingFilter] # Указываем какой класс будет использоваться для фильтра
    filterset_fields = ['status', 'athlete'] # Поля, по которым будет происходить фильтрация
    ordering_fields = ['created_at']

class StartRunView(APIView):
    # def get(self, request):
    #     data = {"message": "GET запрос обработан"}
    #     return Response(data, status=status.HTTP_200_OK)

    def post(self, request, run_id):
        run = get_object_or_404(Run, id=run_id)
        if run.status == 'init':
            run.status = 'in_progress'
            run.save()
            return JsonResponse({"status":f"run with {run_id} in progress"}, status=status.HTTP_200_OK)
        return JsonResponse({"status":f"run with {run_id} not with correct status"}, status=status.HTTP_400_BAD_REQUEST)

class StopRunView(APIView):
    # def get(self, request):
    #     data = {"message": "GET запрос обработан"}
    #     return Response(data, status=status.HTTP_200_OK)

    def post(self, request, run_id):
        run = get_object_or_404(Run, id=run_id)
        if run.status == 'in_progress':
            run.status = 'finished'
            run.save()
            return JsonResponse({"status":f"run with {run_id} finished"}, status=status.HTTP_200_OK)
        return JsonResponse({"status":f"run with {run_id} not with correct status"}, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.filter(is_superuser=False).all()


    serializer_class = UserSerializer


    pagination_class = UserPagination


    filter_backends = [SearchFilter, OrderingFilter] # Подключаем SearchFilter здесь
    search_fields = ['first_name', 'last_name'] # Указываем поля по которым будет вестись поиск
    ordering_fields = ['date_joined']


    def get_queryset(self):
        qs = self.queryset.annotate(
            runs_finished=Count(
                'runs',
                filterr=Q(runs__status='finished')
            )
        )
        user_type = self.request.query_params.get('type', None)
        if user_type == 'coach':
            qs = qs.filter(is_staff=True)
        elif user_type == 'athlete':
            qs = qs.filter(is_staff=False)
        return qs