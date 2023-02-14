from django.urls import path
from onoffled import views

urlpatterns = [
    path('led_on/', views.led_on, name='led_on'),
    path('led_off/', views.led_off, name='led_off'),
    path('led/', views.led, name='led'),
]