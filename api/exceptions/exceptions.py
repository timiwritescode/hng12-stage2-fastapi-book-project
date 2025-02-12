from fastapi import status
from fastapi.exceptions import HTTPException

class AppBaseException(HTTPException):
    """
    Custom application Base Exception class
    """
    def __init__(self, status_code, message):
        super().__init__(
            status_code=status_code,
            detail=message
        )



class BookNotFoundException(AppBaseException):
    """
    Book not found exception

    feat: returns 404 Not Found response with optional custom message for
    un-existent entity
    """
    def __init__(self, message="Book not found"):
        super().__init__(
            status_code= status.HTTP_404_NOT_FOUND,
            message=message
        )