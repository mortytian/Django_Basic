from django.urls import path
from .views import Index
urlpatterns = [
    path('<str:name>', Index.as_view(), name = 'index')
]