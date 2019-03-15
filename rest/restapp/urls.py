from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'hotels'
urlpatterns = [
    path('/', views.HotelList.as_view()),
    path('/<int:pk>/', views.HotelDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)