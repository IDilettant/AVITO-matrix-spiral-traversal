from typing import List

import pytest


@pytest.fixture
def graphic_matrix() -> str:
    """Graphical representation of matrix downloaded from the url."""
    return """+-----+-----+-----+-----+
|  10 |  20 |  30 |  40 |
+-----+-----+-----+-----+
|  50 |  60 |  70 |  80 |
+-----+-----+-----+-----+
|  90 | 100 | 110 | 120 |
+-----+-----+-----+-----+
| 130 | 140 | 150 | 160 |
+-----+-----+-----+-----+
"""


@pytest.fixture
def source_matrix_4_size() -> List[List[int]]:
    """Formatted matrix."""
    return [
        [10, 20, 30, 40],
        [50, 60, 70, 80],
        [90, 100, 110, 120],
        [130, 140, 150, 160],
    ]


@pytest.fixture
def source_matrix_3_size() -> List[List[int]]:
    """Formatted matrix."""
    return [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90],
    ]


@pytest.fixture
def traversal_4_size() -> List[int]:
    """Result of spiral_traversal traversal of matrix."""
    return [
        10, 50, 90, 130,
        140, 150, 160, 120,
        80, 40, 30, 20,
        60, 100, 110, 70,
    ]


@pytest.fixture
def traversal_3_size() -> List[int]:
    """Result of spiral_traversal traversal of matrix."""
    return [
        10, 40, 70,
        80, 90, 60,
        30, 20, 50,
    ]


@pytest.fixture
def server_url() -> str:
    """Url for the matrix download."""
    return 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
