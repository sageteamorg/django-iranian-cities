import uuid
from typing import Optional


class SageError(Exception):
    """Base class for all Sage exceptions.

    Attributes:
        status_code (int): HTTP status code associated with the error.
        default_detail (str): Default error message.
        default_code (str): Default error code.
        section_code (str): Section code for categorizing errors.
        detail (str): Specific error message.
        code (str): Specific error code.
        section_code (str): Section code for the specific error.
        error_id (str): Unique identifier for the error instance.

    Methods:
        __init__(detail: Optional[str] = None, code: Optional[str] = None, section_code: Optional[str] = None):
            Initializes the error with specific details.
        __str__() -> str: Returns a formatted string representation of the error.

    """

    status_code: int = 500
    default_detail: str = "An error occurred."
    default_code: str = "E5000"
    section_code: str = "SAGE"

    def __init__(
        self,
        detail: Optional[str] = None,
        code: Optional[str] = None,
        section_code: Optional[str] = None,
    ):
        self.detail: str = detail if detail is not None else self.default_detail
        self.code: str = code if code is not None else self.default_code
        self.section_code: str = (
            section_code if section_code is not None else self.section_code
        )
        self.error_id: str = str(uuid.uuid4())

    def __str__(self) -> str:
        return f"Error {self.section_code}{self.code} - {self.detail} (Error ID: {self.error_id})"


class IranianCitiesError(SageError):
    """Exception raised for general Iranian Cities errors.

    Inherits from:
        SageError

    Attributes:
        status_code (int): HTTP status code associated with the error.
        default_detail (str): Default error message for Iranian Cities errors.
        default_code (str): Default error code for Iranian Cities errors.
        section_code (str): Section code for Iranian Cities errors.

    """

    status_code: int = 500
    default_detail: str = "A Sage Iranian Cities error occurred."
    default_code: str = "E5001"
    section_code: str = "IC"


class IranianCitiesConfigurationError(IranianCitiesError):
    """Exception raised for Iranian Cities configuration errors.

    Inherits from:
        IranianCitiesError

    Attributes:
        status_code (int): HTTP status code associated with the error.
        default_detail (str): Default error message for configuration errors.
        default_code (str): Default error code for configuration errors.
        section_code (str): Section code for configuration errors.

    """

    status_code: int = 400
    default_detail: str = (
        "Invalid Sage Irianian Cities configuration. Please check your settings."
    )
    default_code: str = "E4001"
    section_code: str = "CFG"
