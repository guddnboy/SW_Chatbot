from django.urls import path
from . import views

app_name = 'chatbotAdmin'

urlpatterns = [
    path('admin_page/', views.admin_page, name='admin_page'),
]