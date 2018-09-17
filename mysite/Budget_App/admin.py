from django.contrib import admin

from .models import Plan,Category,Expense
# Register your models here.

admin.site.register(Plan)
admin.site.register(Category)
admin.site.register(Expense)
