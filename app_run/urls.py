from django.urls import path, include
from app_run.views import company_details_view
from rest_framework.routers import DefaultRouter
from .views import RunViewSet

router = DefaultRouter()
router.register('runs', RunViewSet)

urlpatterns = [
    path('company_details/', company_details_view),
    path('', include(router.urls))
]