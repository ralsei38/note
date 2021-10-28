# from django.http.response import Http404
# from django.http import HttpResponse
# from django.template import loader
from django.http.response import Http404
from django.shortcuts import redirect, render
from .forms import NoteForm, DoneForm
from .models import Note

# Create your views here.
def index(request):
    notes = Note.objects.filter(is_done=0)
    context = {'notes': notes}
    return render(request, 'index.html', context)

def done(request):
    notes = Note.objects.filter(is_done=1)
    context = {'notes': notes}
    return render(request, 'done.html', context)

def form(request):
    context = {}

    if request.method == 'GET':
        form = NoteForm(request.GET)

        if form.is_valid():
            #insert data in db
            #return index page
            form.save()
            return redirect('index')
        else:
            #return blank form
            context = {'form': NoteForm()}
            return render(request, 'form.html', context)
    else:
        raise 'help'

def add(request):
    context = {}
    return render(request, 'index.html', context)

def delete(request, id):
    if request.method == 'GET':
        note = Note.objects.filter(pk=id)
        note.delete()
    else:
        Http404()
    return redirect('done')


def set_as_done(request, id):
    if request.method == 'GET':
        note = Note.objects.filter(pk=id)[0]
        note.is_done = 1
        note.save()
        print(note)
    else:
        Http404()
    return redirect('index')

def categories(request):
    context = {}
    return render(request, 'categories.html', context)