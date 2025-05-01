from django_core.exceptions import AppValidationError


class NoteNotOwner(AppValidationError):
    status_code = 400
    default_detail = "Note not owned by user"
    default_code = "note_not_owned_by_user"