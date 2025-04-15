from django_core.exceptions import AppValidationError


class EmailRequired(AppValidationError):
    status_code = 400
    default_detail = "Email is required"
    default_code = "email_required"


class FullNameRequired(AppValidationError):
    status_code = 400
    default_detail = "Full name is required"
    default_code = "full_name_required"
