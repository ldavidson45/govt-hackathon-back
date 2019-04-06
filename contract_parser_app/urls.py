from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('detail/', views.contract_detail, name="contract_detail")
]