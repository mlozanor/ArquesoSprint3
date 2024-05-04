from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('documentos/', views.documento_list),
    path('documentoscreate/', csrf_exempt(views.documento_create), name='documentoCreate'),
]