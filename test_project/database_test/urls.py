from django.urls import path
from .views import DB, second_page, contact

urlpatterns = [
    path('home/', DB, name='home'),
    path('home/new/', second_page, name='new'),
    path('contact/', contact, name='contact'),
]
