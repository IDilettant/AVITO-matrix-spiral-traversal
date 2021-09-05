"""Matrix spiral traversal library.

Get a square matrix from a remote server and return the result of
traversing the matrix in a spiral traverse: counterclockwise, starting from
the upper left corner
"""
import logging
from typing import List

from aiohttp import ClientError, ClientSession
from exceptions import FormatMatrixExceptions, GetMatrixException


async def get_matrix(url: str, raise_on_error: bool = False) -> List[int]:
    """Get the result of traversing a matrix downloaded from a remote server.

    Args:
        url: remote server url
        raise_on_error: flag of raising exception of network access

    Returns:
        the matrix traversing result

    Raises:
        GetMatrixException: exception of network access
        FormatMatrixExceptions: exception of matrix source format
    """
    logger = logging.getLogger(__name__)
    try:
        graphic_matrix = await download_matrix(url)
    except ClientError as exc:
        if raise_on_error:
            raise GetMatrixException("Download can't be finished") from exc
        logger.warning(exc)
        return []
    if not _is_right_format(graphic_matrix):
        if raise_on_error:
            raise FormatMatrixExceptions('Unexpected matrix format')
        logger.warning(FormatMatrixExceptions('Unexpected matrix format'))
        return []
    matrix = format_matrix(graphic_matrix)
    return traverse_matrix(matrix)


async def download_matrix(url: str) -> str:
    """Download graphic matrix from a remote server.

    Args:
        url: remote server url

    Returns:
        graphic matrix
    """
    async with ClientSession(raise_for_status=True) as session:
        async with session.get(url) as resp:
            return await resp.text()


def traverse_matrix(source_matrix: List[List[int]]) -> List[int]:
    """Collect matrix values.

    Traverse in a spiral_traversal counterclockwise,
    starting from the upper left corner

    Args:
        source_matrix: the matrix in list format

    Returns:
        result of matrix traverse
    """
    traverse: List[int] = []
    matrix = list(zip(*source_matrix))
    while matrix:
        traverse.extend(matrix.pop(0))
        matrix = list(zip(*matrix))[::-1]
    return traverse


def format_matrix(graphic_matrix: str) -> List[List[int]]:
    """Format graphical representation of the matrix to list.

    Args:
        graphic_matrix: graphical representation of the matrix

    Returns:
        the matrix in list format
    """
    matrix_lines = graphic_matrix.split('\n')
    return [
        [
            int(char)
            for char in line.split(' ')
            if char.isdigit()
        ]
        for index, line in enumerate(matrix_lines)
        if index % 2 == 1 and line
    ]


def _is_right_format(matrix: str) -> bool:  # noqa: WPS210
    """Check the matrix format for compliance with the expected.

    Args:
        matrix: graphical representation of the matrix

    Returns:
        bool

    Expected format example:
        +-----+-----+
        |  10 |  20 |
        +-----+-----+
        |  30 |  40 |
        +-----+-----+
    """
    if isinstance(matrix, str) and matrix:
        checks = []
        matrix_lines = matrix.strip().split('\n')
        upper_borderline = matrix_lines[0]
        size = len([char for char in upper_borderline.split('+') if char != ''])
        for index, line in enumerate(matrix_lines):
            if index % 2 == 0:
                checks.append(line == upper_borderline)
            if index % 2 == 1:
                checks.append(
                    len(
                        [
                            int(char)
                            for char in line.split(' ')
                            if char.isdigit()
                        ],
                    ) == size,
                )
        return all(checks)
    return False
