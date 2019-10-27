from django.contrib import admin
from .models import StudentBasicInfo

# Register your models here.


class StudentBasicInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'student_id','email','phone']
    search_fields = ('name', 'student_id', 'phone', 'email',)


admin.site.register(StudentBasicInfo, StudentBasicInfoAdmin)