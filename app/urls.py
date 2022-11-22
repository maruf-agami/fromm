from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('registration', views.registration, name='registration'),
    path('add_formfillup', views.add_formfillup, name='add_formfillup'),
    path('forms', views.view_form, name='view_form'),
    path('send/<int:form_id>', views.change_step, name='send'),
    path('add_payment/<int:form_id>', views.add_payment, name='add_payment'),
]