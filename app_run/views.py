from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Run
from .serializers import RunSerializer
from django.conf import settings


@api_view(['GET'])
def company_details_view(request):
    details = {'company_name': "Забег за пивом",
               'slogan': 'Беги Форест, беги',
               'contacts': 'КБшечка у дома'}
    return Response(details)


class RunViewSet(viewsets.ModelViewSet):
    queryset = Run.objects.all()
    serializer_class = RunSerializer
