from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings


@api_view(['GET'])
def company_details_view(request):
    details = {'company_name': "Забег за пивом",
               'slogan': 'Беги Форест, беги',
               'contacts': 'КБшечка у дома'}
    return Response(details)