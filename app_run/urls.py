from django.urls import path, include
from app_run.views import company_details_view
from rest_framework.routers import DefaultRouter
from .views import RunViewSet, UserViewSet, StartRunView, StopRunView

router = DefaultRouter()
router.register('runs', RunViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('company_details/', company_details_view),
    path('', include(router.urls)),
    path('runs/<int:run_id>/start/', StartRunView.as_view()),
    path('runs/<int:run_id>/stop/', StopRunView.as_view()),
]