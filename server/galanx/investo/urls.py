from django.urls import path, include 

urlpatterns = [
    path('/', include('stocky.urls')),
]
