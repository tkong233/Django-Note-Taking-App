from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Note

def index(request):
    notes = Note.objects.all()
    context = {'notes': notes}
    return render(request, 'notes/index.html', context)

def add(request):
    try:
        new_note_text = request.POST['new_note']
    except KeyError:
        raise("No note to add")
    else:
        n = Note(text=new_note_text)
        n.save()
        return HttpResponseRedirect(reverse('notes:index'))