from django.contrib import admin
from . models import BlogPost, Service, ServiceCategory
# Register your models here.

admin.site.register(BlogPost)

admin.site.register(ServiceCategory)
admin.site.register(Service)
