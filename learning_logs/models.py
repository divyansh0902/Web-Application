from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    #topic user is learning
    text = models.CharField(max_length=200) #CharField used when we want to store small amount of text. we also tell django how much space it should reserve in datanase.
    date_added = models.DateTimeField(auto_now_add=True) #DateTimeField record date and time. we pass argument auto_now_add=true which set this attribute to curent time and date
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        #return a string representation of model
        return self.text

class Entry(models.Model):
    #something specific learned about topic
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) #foreign key is a database term, it's a reference to another record in database. it connects each entry to specific topic
                                                               #on_delete=models.CASCADE tells django that when topic is deleted all entrie associated with that topic should be deleted
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta: #contains extra info for manageing a model
        verbose_name_plural = 'entries' #tells django to use entries when refering to more than one entry

    def __str__(self): #tells django which info to show when refers to individual entries
        #return a string representation of model
        return f"{self.text[:50]}..." #we tell django to show first 50 characters of text