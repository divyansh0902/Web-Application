from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import Http404

from learning_logs.forms import TopicForm
from .models import Topic, Entry
from .forms import EntryForm, TopicForm

def index(request):
    #home page for learning_logs
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    #show all topics
    topics = Topic.objects.filter(owner=request.user).order_by('date_added') #when user logged in, request gas request.user attribute that stores info about the user. Topic.objects.filter(owner=request.user) tells django tp retrive only topic objects from databaste whose owner attribute mattches the current user
    topics = Topic.objects.order_by('date_added') #query database by asking for Topic objects,sorted by date_added attribute
    context = {'topics': topics} #define context that we wills end to template
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    #show a single and all its entries
    topic = Topic.objects.get(id=topic_id) #query database by asking for Topic objects,sorted by date_added attribute
    #make sure topic belongs to current user
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries} #define context that we wills end to template
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    #add new topic
    if request.method != 'POST': #determines whether request method is GET or POST
        #no data submitted; create a blank form
        form = TopicForm()
    else:
        #POST data submitted; process data
        form = TopicForm(data=request.POST)
        if form.is_valid(): #checks that all required fields have been filled in and the data entered matches the field types expected
            new_topic = form.save(commit=False)
            new_topic.owner = request.user #set new topic's owner attribute to current user
            new_topic.save()
            return redirect('learning_logs:topics')


    #display a blank or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    #add new enrty for a particular topic
    topic = Topic.objects.get(id=topic_id) #use topic_id to get correct topic object

    if request.method != 'POST': #determines whether request method is GET or POST. if block executed if it's a GET request
        #no data submitted; create a blank form
        form = EntryForm()
    else: 
        #POST data submitted; process data
        form = EntryForm(data=request.POST)
        if form.is_valid(): #check whether the form is valid
            new_entry = form.save(commit=False) #false tells django to create new entry object and assign it to new_entry without saving it to database yet
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    #display a blank or invalid form
    context = {'topic': topic,'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    #edit existing entry
    entry = Entry.objects.get(id=entry_id) #get entry object that user wants to edit and topic associated with it
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST': #determines whether request method is GET or POST. if block executed if it's a GET request
        #iniial request; pre - fill with the current entry
        form = EntryForm(instance=entry) 
    else: 
        #POST data submitted; process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid(): #check whether the form is valid
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id) #redirect to topic page where user should see updated version of entry they edited

    #display a blank or invalid form
    context = {'entry': entry, 'topic': topic,'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
    