from django.contrib import admin
from .models import Status, Orders, CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'patronymic', 'email', 'phone', 'is_staff')
    list_display_links = ('id', 'username', 'first_name', 'last_name', 'patronymic', 'email', 'phone', 'is_staff')


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'status', 'phone',  'orderdatetime',  'description')
    list_display_links = ('id', 'owner', 'status', 'phone',  'orderdatetime',  'description')


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')



