from django.contrib import admin
from .models import Slam_session, Judges_scores, Poet

class Poet_inline(admin.TabularInline):
	model = Poet

class Slam_session_inline(admin.ModelAdmin):
	inlines = [
		Poet_inline
	]

admin.site.register(Slam_session, Slam_session_inline)
admin.site.register(Judges_scores)
admin.site.register(Poet)
