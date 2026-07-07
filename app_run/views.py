from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()  # Указываем разрешённые методы
def company_details_view(request):
    return Response({
        'company_name': 'Бегуны Димы Мира',
        'slogan': 'Бегаем за пивом',
        'contacts': 'Город СПб, КБ у дома'
    })
