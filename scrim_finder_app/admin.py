from django.contrib import admin
from scrim_finder_app.models import *

class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('game',)}

class TeamAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Team, TeamAdmin)
admin.site.register(userProfile)
admin.site.register(Games, GameAdmin)
admin.site.register(Match)
