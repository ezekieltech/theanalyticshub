from django.contrib import admin
from .models import Post, Service, Industry

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'sales_point')
    list_filter = ("name",)


admin.site.register(Service, ServiceAdmin)


class IndustryAdmin(admin.ModelAdmin):
    pass
    # list_display = ('name', 'focus')
    # list_filter = ("name",)


admin.site.register(Industry, IndustryAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('firstname',)
