"""Main tests."""
import pook
import pytest
from mattrav.exceptions import FormatMatrixExceptions, GetMatrixException
from mattrav.matrix_traversal import get_matrix

GRAPHICAL_MATRIX_4_SIZE = """+-----+-----+-----+-----+
|  10 |  20 |  30 |  40 |
+-----+-----+-----+-----+
|  50 |  60 |  70 |  80 |
+-----+-----+-----+-----+
|  90 | 100 | 110 | 120 |
+-----+-----+-----+-----+
| 130 | 140 | 150 | 160 |
+-----+-----+-----+-----+
"""
GRAPHICAL_MATRIX_3_SIZE = """+-----+-----+-----+
|  10 |  20 |  30 |
+-----+-----+-----+
|  40 |  50 |  60 |
+-----+-----+-----+
|  70 |  80 |  90 |
+-----+-----+-----+
"""
GRAPHICAL_MATRIX_WRONG = """|-----|-----|-----|
|  10 |  20 |  30 |
|-----|-----|-----|
"""
TRAVERSAL_4_SIZE = [
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70,
]
TRAVERSAL_3_SIZE = [
    10, 40, 70,
    80, 90, 60,
    30, 20, 50,
]
SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'status_code, matrix, traversal',
    [
        (200, GRAPHICAL_MATRIX_4_SIZE, TRAVERSAL_4_SIZE),
        (200, GRAPHICAL_MATRIX_3_SIZE, TRAVERSAL_3_SIZE),
    ],
)
async def test_get_matrix(status_code, matrix, traversal):
    with pook.use():
        pook.get(
            SOURCE_URL,
            reply=status_code,
            response_json=matrix,
        )
        assert await get_matrix(SOURCE_URL) == traversal


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'status_code, matrix, exception',
    [
        (200, GRAPHICAL_MATRIX_WRONG, FormatMatrixExceptions),
        (204, '', FormatMatrixExceptions),
        (400, '', GetMatrixException),
        (500, '', GetMatrixException),
    ],
)
async def test_get_matrix_exc(status_code, matrix, exception):
    with pook.use():
        pook.get(
            SOURCE_URL,
            reply=status_code,
            response_json=matrix,
        )
        with pytest.raises(exception):
            await get_matrix(SOURCE_URL, raise_on_error=True)
