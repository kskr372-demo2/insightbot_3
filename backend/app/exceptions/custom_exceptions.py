class FileTooLargeException(Exception):
    """Raised when uploaded file exceeds maximum size."""

    pass


class UnsupportedFileTypeException(Exception):
    """Raised when uploaded file type is invalid."""

    pass


class EmptyFileException(Exception):
    """Raised when uploaded file is empty."""

    pass