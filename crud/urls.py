from django.urls import path,include
from . import views
# from rest_framework.views import 


urlpatterns = [
    path('',views.Student_details.as_view(),name='student'),
    path('<int:pk>/',views.Student_updates.as_view(),name='student'),
    path('auth/',include('rest_framework.urls')),
]   