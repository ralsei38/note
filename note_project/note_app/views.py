# from django.http.response import Http404
# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from .forms import NoteForm
from .models import Note

# Create your views here.
def index(request):
    notes = Note.objects.all()
    context = {'notes': notes}
    return render(request, 'index.html', context)

def form(request):
    context = {}

    if request.method == 'GET':
        form = NoteForm(request.GET)

        if form.is_valid():
            #insert data in db
            #return index page
            form.save()
            return index(request)
        else:
            #return blank form
            context = {'form': NoteForm()}
            return render(request, 'form.html', context)
    else:
        raise 'help'

def add(request):
    context = {}
    return render(request, 'index.html', context)

def set_as_done(request):
    return index(request)