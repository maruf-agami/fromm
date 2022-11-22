from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('registration', views.registration, name='registration'),
    path('add_formfillup', views.add_formfillup, name='add_formfillup'),
    path('forms', views.view_form, name='view_form'),
]