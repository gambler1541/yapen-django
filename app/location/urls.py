from django.urls import path

from .views import location_list

appname = 'location'
urlpatterns = [
    path('', location_list, name='location-list'),

]