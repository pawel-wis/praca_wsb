from django.urls import path
from . import views

# here are url patterns
urlpatterns = [
    #/
    path('', views.index, name="index")
]