from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from .models import Sensor, Measurement
from .serializers import SensorChangeSerializer, MeasurementSerializer, SensorDetailSerializer


class SensorsListCreateView(ListCreateAPIView):
    """
    Create a sensor. Enter the name and description (optional parameter) 
    of the sensor
    and
    Get a list of sensors. A list is displayed with brief information on 
    the sensors: ID, name and description (if specified)
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorChangeSerializer


class SensorСhangeView(RetrieveUpdateAPIView):
    """
    Сhange a sensor. Enter the name and description (optional parameter) 
    of the sensor
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorChangeSerializer


class SensorInfoView(RetrieveUpdateAPIView):
    """
    Get information on one sensor. Complete information on the sensor: 
    ID, name, description (if specified) and a list of all measurements 
    with temperature and time.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementCreateView(CreateAPIView):
    """
    Add a measurement. Specify sensor ID and temperature
    """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

