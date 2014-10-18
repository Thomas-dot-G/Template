<<<<<<< HEAD
from django.contrib import admin
from project.models import *

class ParticipationInline(admin.TabularInline):
    model = Participation
    extra = 1

class PlayerAdmin(admin.ModelAdmin):
    inlines = (ParticipationInline,)

class MatchAdmin(admin.ModelAdmin):
    inlines = (ParticipationInline,)

# Register your models here.
admin.site.register(Player, PlayerAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Participation)
=======
from django.contrib import admin
from project.models import *

class ParticipationInline(admin.TabularInline):
    model = Participation
    extra = 1

class PlayerAdmin(admin.ModelAdmin):
    inlines = (ParticipationInline,)

class MatchAdmin(admin.ModelAdmin):
    inlines = (ParticipationInline,)


# Register your models here.
admin.site.register(Player, PlayerAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Participation)
admin.site.register(Team)
admin.site.register(Account)
admin.site.register(Log)
>>>>>>> f77d550abe9dd589ee50ca1674a7b858df54c566
