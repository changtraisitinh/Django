from django.contrib import admin
from .models import (Employees, Departments, DeptEmp, DeptManager, Salaries, Titles)
from .forms import EmployeeForm
from django.contrib.admindocs import AdminSite 
from django.utils.translation import ugenttext_lazy
class MyEmsAdminSite(AdminSite):
    site_title = ugenttext_lazy('test Django site admin')
    site_header = ugenttext_lazy('test Django administration')
    index_title = ugenttext_lazy('test Site administration')

my_ems_admin_site = MyEmsAdminSite

class GenderFilter(admin.SimpleListFilter):
    title = 'Gender'
    parameter_name = 'gender'

    def lookups(self, request, modeladmin):
        return (
            ('M', 'Male'),
            ('F', 'Female'),
        )
    
    def queryset(self, request, queryset):
        return queryset.filter(gender__exact=self.value()) if self.value() else queryset

class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeForm
    search_fields = ('emp_no', 'first_name', 'last_name', 'hire_date', 'gender')
    list_display = ('emp_no', 'first_name', 'last_name', 'hire_date', 'gender')
    list_display_links = ('emp_no',)
    list_filter = ('hire_date', GenderFilter, )
    save_on_top = True
    actions_on_bottom = False
    ordering = ('-hire_date',)


# admin.site.register(Employees, EmployeeAdmin)
# admin.site.register(Departments)
# admin.site.register(DeptEmp)
# admin.site.register(DeptManager)
# admin.site.register(Salaries)
# admin.site.register(Titles)

my_ems_admin_site.site.register(Employees, EmployeeAdmin)
my_ems_admin_site.site.register(Departments)
my_ems_admin_site.site.register(DeptEmp)
my_ems_admin_site.site.register(DeptManager)
my_ems_admin_site.site.register(Salaries)
my_ems_admin_site.site.register(Titles)