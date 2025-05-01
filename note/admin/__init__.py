from django.contrib import admin

from note.admin.note_admin import NoteAdmin
from note.models.note_model import Note

admin.site.register(Note, NoteAdmin)