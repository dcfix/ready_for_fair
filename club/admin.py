from django.contrib import admin

# Register your models here.
from .models import Club
from .models import Group
from .models import Member
from .models import Project

admin.site.register(Club)
admin.site.register(Project)
admin.site.register(Group)
admin.site.register(Member)
