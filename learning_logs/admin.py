from django.contrib import admin

from .models import Topic, Entry #dot tells django to look for models.py in same directory as admin.py
admin.site.register(Topic) #tells django to manage our model through admin site
admin.site.register(Entry)