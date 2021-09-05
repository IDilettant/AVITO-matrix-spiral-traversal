from typing import List

import pytest
from spiral_traversal.solution import (
    _is_right_format,
    download_matrix,
    format_matrix,
    get_matrix,
    traverse_matrix,
)


@pytest.mark.asyncio
async def test_download_matrix(server_url: str, graphic_matrix: str):
    assert await download_matrix(server_url) == graphic_matrix


def test_is_right_format(graphic_matrix: str):
    assert _is_right_format(graphic_matrix)


def test_format_graphic_matrix(
        graphic_matrix: str,
        source_matrix_4_size: List[List[int]],
):
    assert format_matrix(graphic_matrix) == source_matrix_4_size


def test_traverse_matrix_4_size(
        source_matrix_4_size: List[List[int]],
        traversal_4_size: List[int],
):
    assert traverse_matrix(source_matrix_4_size) == traversal_4_size


def test_traverse_matrix_3_size(
        source_matrix_3_size: List[List[int]],
        traversal_3_size: List[int],
):
    assert traverse_matrix(source_matrix_3_size) == traversal_3_size


@pytest.mark.asyncio
async def test_get_matrix(traversal_4_size: List[int], server_url: str):
    assert await get_matrix(server_url) == traversal_4_size
