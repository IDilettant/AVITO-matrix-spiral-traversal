"""Main tests."""
import pook
import pytest
from mattrav.exceptions import FormatMatrixExceptions, GetMatrixException
from mattrav.matrix_traversal import get_matrix

GRAPHIC_MATRIX_4_SIZE = """+-----+-----+-----+-----+
|  10 |  20 |  30 |  40 |
+-----+-----+-----+-----+
|  50 |  60 |  70 |  80 |
+-----+-----+-----+-----+
|  90 | 100 | 110 | 120 |
+-----+-----+-----+-----+
| 130 | 140 | 150 | 160 |
+-----+-----+-----+-----+
"""
GRAPHIC_MATRIX_3_SIZE = """+-----+-----+-----+
|  10 |  20 |  30 |
+-----+-----+-----+
|  40 |  50 |  60 |
+-----+-----+-----+
|  70 |  80 |  90 |
+-----+-----+-----+
"""
GRAPHIC_MATRIX_WRONG = """|-----|-----|-----|
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
async def test_get_matrix():
    with pook.use(network=True):
        pook.get(
            SOURCE_URL,
            reply=200,
            response_json=GRAPHIC_MATRIX_4_SIZE,
        )
        assert await get_matrix(SOURCE_URL) == TRAVERSAL_4_SIZE

        pook.get(
            SOURCE_URL,
            reply=200,
            response_json=GRAPHIC_MATRIX_3_SIZE,
        )
        assert await get_matrix(SOURCE_URL) == TRAVERSAL_3_SIZE

        pook.get(
            SOURCE_URL,
            reply=200,
            response_json=GRAPHIC_MATRIX_WRONG,
        )
        with pytest.raises(FormatMatrixExceptions) as exc:
            await get_matrix(SOURCE_URL, raise_on_error=True)
        assert str(exc.value) == 'Unexpected matrix format'

        pook.get(
            SOURCE_URL,
            reply=204,
        )
        with pytest.raises(FormatMatrixExceptions) as exc:
            await get_matrix(SOURCE_URL, raise_on_error=True)
        assert str(exc.value) == 'Unexpected matrix format'

        pook.get(
            SOURCE_URL,
            reply=400,
        )
        with pytest.raises(GetMatrixException) as exception:
            await get_matrix(SOURCE_URL, raise_on_error=True)
        assert str(exception.value) == "Download can't be finished"

        pook.get(
            SOURCE_URL,
            reply=500,
        )
        with pytest.raises(GetMatrixException) as exception:
            await get_matrix(SOURCE_URL, raise_on_error=True)
        assert str(exception.value) == "Download can't be finished"
