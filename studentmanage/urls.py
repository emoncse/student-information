from django.urls import path
from .views import StudentsBasicInfoViewSet

urlpatterns = [
    path('students', StudentsBasicInfoViewSet.as_view({'get': 'list'}), name='students-list'),
    path('students/<id>', StudentsBasicInfoViewSet.as_view({'get': 'retrieve'}), name='students-details'),
]
