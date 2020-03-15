from django.urls import path
from .views import home, second_page, contact,signuppage, landingpage, datepage

urlpatterns = [
    path('home/', home, name='home'),
    path('home/new/', second_page, name='new'),
    path('contact/', contact, name='contact'),
    path('date/<int:year>/', datepage, name='datepage'),
    path('signup/', signuppage, name='signuppage'),
    path('', landingpage, name='landingpage')
]
