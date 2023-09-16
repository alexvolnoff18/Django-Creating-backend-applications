
from django.urls import path

from .views import SensorsListCreateView, SensorСhangeView, SensorInfoView, MeasurementCreateView


urlpatterns = [
    path('sensors/', SensorsListCreateView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
    path('sensors/update/<pk>/', SensorСhangeView.as_view()),
    path('sensors/<pk>/', SensorInfoView.as_view())
]
