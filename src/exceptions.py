class HeygenAPIError(Exception):
    """
    Raised when the Heygen API returns an error.
    """

    error_prefix = "Heygen API Error:"

    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code
        super().__init__(f"{self.error_prefix} {message}")


class HeygenUnexpectedError(Exception):
    """
    Raised when the Heygen API returns an unexpected error.
    """

    error_prefix = "Heygen Unexpected Error:"

    def __init__(self, message: str):
        self.message = message
        super().__init__(f"{self.error_prefix} {message}")
