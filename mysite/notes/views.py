from django.shortcuts import render
from django.http import HttpResponse
from .models import Note

def index(request):
    notes = Note.objects.all()
    context = {'notes': notes}
    return render(request, 'notes/index.html', context)
