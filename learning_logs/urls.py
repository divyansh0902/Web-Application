'''defines URL pattern for learning_logs'''
from django.urls import path #needed when mapping URLs to views
from . import views #dot tells python to import views.py module from same directory

app_name= 'learning_logs' #helps django distinguish this file with other file of same name

#variable urlpattern is a list of individual pages that can be requested from learning_logs app
urlpatterns = [
    #home page
    path('', views.index, name='index'),
    #page that shows all topics
    path('topics/', views.topics, name='topics'),
    #detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #page for adding new topic
    path('new_topic/', views.new_topic, name= 'new_topic'),
    #page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #page for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]