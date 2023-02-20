from django.urls import path
from thumbnails import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('thumbnails/', views.ThumbnailList.as_view()),
    path('thumbnails/<int:pk>/', views.ThumbnailDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
