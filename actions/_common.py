"""Shared implementation behind the named, dedicated click functions."""

from typing import TypeAlias

from core.image import find_image
from core.mouse import click_point

Point: TypeAlias = tuple[int, int]


def click_template(image_name: str, force_coordinate: Point | None = None) -> Point:
    """Click a forced point or find and click a named template.

    Each public action keeps its own force variable so it can later be changed
    independently even where multiple actions share the same image.
    """
    if force_coordinate is not None:
        click_point(*force_coordinate)
        return force_coordinate
    point = find_image(f"imgs/{image_name}")
    if point is None:
        raise TimeoutError(f"Could not find {image_name}")
    click_point(*point)
    return point
