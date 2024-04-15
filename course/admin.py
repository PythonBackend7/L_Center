from django.contrib import admin
from .models import Course, Teacher


# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'name', 'email')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'teacher', 'price')
    list_display_links = ('id', 'name', 'teacher', 'price')
    search_fields = ('name', 'teacher')


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course, CourseAdmin)