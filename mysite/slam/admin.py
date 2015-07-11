from django.contrib import admin

from .models import Slam_session, Judges_scores, Poet

admin.site.register(Slam_session)
admin.site.register(Judges_scores)
admin.site.register(Poet)