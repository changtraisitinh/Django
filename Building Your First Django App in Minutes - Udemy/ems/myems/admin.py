from django.contrib import admin
from .models import (Employees, Departments, DeptEmp, DeptManager, Salaries, Titles)

admin.site.register(Employees)
admin.site.register(Departments)
admin.site.register(DeptEmp)
admin.site.register(DeptManager)
admin.site.register(Salaries)
admin.site.register(Titles)
