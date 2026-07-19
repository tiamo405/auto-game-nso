"""Shared implementation behind the named, dedicated click functions."""

from typing import TypeAlias

from core.image import find_image
from core.mouse import click_point, click_point_hold

Point: TypeAlias = tuple[int, int]


def click_template(
    image_name: str,
    force_coordinate: Point | None = None,
    hold_seconds: float | None = None,
) -> Point:
    """Click a forced point or find and click a named template.

    Each public action keeps its own force variable so it can later be changed
    independently even where multiple actions share the same image.
    """
    point = force_coordinate
    if point is None:
        point = find_image(f"imgs/{image_name}")
    if point is None:
        raise TimeoutError(f"Could not find {image_name}")
    if hold_seconds is None:
        click_point(*point)
    else:
        click_point_hold(*point, hold_seconds)
    return point
