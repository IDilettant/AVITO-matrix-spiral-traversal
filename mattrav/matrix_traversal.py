"""Matrix spiral traversal library.

Get a square matrix from a remote server and return the result of
traversing the matrix in a spiral traverse: counterclockwise, starting from
the upper left corner
"""
import logging
from typing import List

from aiohttp import ClientError, ClientSession
from mattrav.exceptions import FormatMatrixExceptions, GetMatrixException

LOGGER = logging.getLogger(__name__)


async def get_matrix(url: str, raise_on_error: bool = False) -> List[int]:
    """Get the result of traversing a matrix downloaded from a remote server.

    Args:
        url: remote server url
        raise_on_error: flag of raising exception of network access

    Returns:
        the matrix traversing result

    Raises:
        GetMatrixException: exception of network access
    """
    try:  # noqa: WPS229
        graphic_matrix = await download_matrix(url)
        matrix = format_matrix(graphic_matrix)
    except ClientError as exc:
        if raise_on_error:
            raise GetMatrixException("Download can't be finished") from exc
        LOGGER.warning(exc)
        return []
    except FormatMatrixExceptions as exc:
        if raise_on_error:
            raise
        LOGGER.warning(exc)
        return []
    return traverse_matrix(matrix)


async def download_matrix(url: str) -> str:
    """Download graphic matrix from a remote server.

    Args:
        url: remote server url

    Returns:
        graphic matrix
    """
    async with ClientSession() as session:
        async with session.get(url) as resp:
            resp.raise_for_status()
            return await resp.text()


def traverse_matrix(source_matrix: List[List[int]]) -> List[int]:
    """Collect matrix values.

    Traverse in a spiral counterclockwise,
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


def format_matrix(graphic_matrix: str) -> List[List[int]]:  # noqa: WPS210
    """Format graphical representation of the matrix to list.

    Args:
        graphic_matrix: graphical representation of the matrix

    Returns:
        the matrix in list format

    Raises:
        FormatMatrixExceptions: exception of matrix source format
    """
    if isinstance(graphic_matrix, str) and graphic_matrix:
        matrix_lines = graphic_matrix.split('\n')
        upper_borderline = matrix_lines[0]
        size = len([char for char in upper_borderline.split('+') if char != ''])
        matrix = [
            [
                int(char)
                for char in line.split(' ')
                if char.isdigit()
            ]
            for index, line in enumerate(matrix_lines)
            if index % 2 == 1 and line
        ]
        if list(filter(lambda line: len(line) == size, matrix)):
            return matrix
    raise FormatMatrixExceptions('Unexpected matrix format')
