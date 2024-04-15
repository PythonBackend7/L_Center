from django.urls import path
from .views import home_view, courselist_view, course_detail_view, teachers_list_view, teachers_detail_view

urlpatterns = [
    path('', home_view, name='home'),
    path('courselist/', courselist_view, name='courselist'),
    path('teachers/', teachers_list_view, name='teachers_list'),
    path('courselist/<int:pk>/', course_detail_view, name='course_detail'),
    path('teachers/<int:pk>/', teachers_detail_view, name='teacher_detail'),
]
