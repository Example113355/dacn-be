from django.urls import path

from note.views.note_view import NoteView

urlpatterns = [
    path(
        "",
        NoteView.as_view({"get": "list", "post": "create", "patch": "update"}),
        name="note"
    )
]