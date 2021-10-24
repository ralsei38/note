from django.forms import ModelForm
from .models import Note

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'desc', 'is_done']

class DoneFOrm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'desc', 'is_done']