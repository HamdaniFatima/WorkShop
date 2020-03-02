from django.contrib import admin
from stories.models import registration
from stories.models import Post



# Register your models here.

admin.site.register(registration)
admin.site.register(Post)