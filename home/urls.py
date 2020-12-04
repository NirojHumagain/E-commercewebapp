from django.urls import path,include
from .views import HomeBaseView
app_name = 'home'
urlpatterns = [

    path('', HomeBaseView.as_view(),name = 'home'),
]