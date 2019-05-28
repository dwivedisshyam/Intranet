from django.contrib import admin

# Register your models here.
from IntranetUser.models import SubMenu, Menu, SubCategory, Category

admin.site.register(Menu)
admin.site.register(SubMenu)
admin.site.register(Category)
admin.site.register(SubCategory)
