from django.contrib import admin
from .models import Team, Work, Comment, Game, Video, Model3D

# Register your models here.

admin.site.register(Team)
admin.site.register(Work)
admin.site.register(Comment)
admin.site.register(Game)
admin.site.register(Video)
admin.site.register(Model3D)
