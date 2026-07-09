from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Run
from .serializers import RunSerializer, UserSerializer
from django.conf import settings


@api_view(['GET'])
def company_details_view(request):
    details = {'company_name': "Забег за пивом",
               'slogan': 'Беги Форест, беги',
               'contacts': 'КБшечка у дома'}
    return Response(details)


class RunViewSet(viewsets.ModelViewSet):
    queryset = Run.objects.select_related('athlete').all()
    serializer_class = RunSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.filter(is_superuser=False)
    serializer_class = UserSerializer

    def get_queryset(self):
        qs = self.queryset
        user_type = self.request.query_params.get('type', None)
        if user_type == 'coach':
            qs = qs.filter(is_staff=True)
        elif user_type == 'athlete':
            qs = qs.filter(is_staff=False)
        return qs
