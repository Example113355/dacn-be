from django_core.exceptions import AppValidationError

class AddressNotFound(AppValidationError):
    status_code = 404
    default_detail = "Address not found"
    default_code = "address_not_found"
    
class AddressAlreadyExists(AppValidationError):
    status_code = 400
    default_detail = "Address already exists"
    default_code = "address_already_exists"
    
class AddressNotOwner(AppValidationError):
    status_code = 400
    default_detail = "Address not owned by user"
    default_code = "address_not_owned_by_user"