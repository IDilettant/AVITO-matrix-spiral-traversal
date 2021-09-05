"""Exceptions module."""


class MatrixException(Exception):
    """Base library exception."""
    pass


class GetMatrixException(MatrixException):
    """Exception of network access."""
    pass


class FormatMatrixExceptions(MatrixException):
    """Exception of matrix source format."""
    pass
