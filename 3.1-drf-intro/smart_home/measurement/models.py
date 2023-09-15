from django.db import models


from django.utils import timezone


class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название датчика')
    description = models.CharField(max_length=100, blank=True, default='',
                                   verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
        ordering = ['-id', 'name']

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, verbose_name='Датчик',
                               related_name='measurement')
    temperature = models.FloatField(verbose_name='Температура, оС')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время измерения')
    image = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name = 'Показание'
        verbose_name_plural = 'Показания'
        ordering = ['sensor', 'created_at']


